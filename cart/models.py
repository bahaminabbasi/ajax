from django.db import models
from django.contrib.auth.models import User

from products.models import Product



class OrderManager(models.Manager):
    def new_or_get(self, request):
        if request.user.is_authenticated:
            user = request.user
            order_obj, created = Order.objects.get_or_create(user=user, status='pending')
            # print('session order id', request.session['order_id'])
            session_order_id = request.session.get('order_id', None)
            if session_order_id is not None:
                qs = self.get_queryset().filter(id=session_order_id)
                session_order_obj = qs.first()
                print('order in session, obj: ', session_order_obj)
                if session_order_obj is not None:
                    session_items = session_order_obj.orderitem_set.all()
                    items = order_obj.orderitem_set.all()
                    for session_item in session_items:
                        found = False
                        for item in items:
                            if item.product.title == session_item.product.title:
                                found = True
                                item.quantity = item.quantity + session_item.quantity
                                item.save()
                        if not found:
                            session_item.order = order_obj
                            session_item.save()
                    request.session.pop('order_id')
                    session_items.delete()
                    session_order_obj.delete()
            else:
                print('session_order_id was None!')   
        else:
            order_obj, created = Order.objects.get_or_create(user=None, status='pending')
            request.session['order_id'] = order_obj.id
        return order_obj, created

    


class Order(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    date_orderd = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, blank=True, null=True)
    transaction_id = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    reserved = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity  for item in orderitems])
        return total

    objects = OrderManager()

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.title} {self.quantity} for {self.order}'

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
#     name = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200, null=True)

#     def __str__(self):
#         return self.name
