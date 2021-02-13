from django.db import models
from django.contrib.auth.models import User

from products.models import Product



class OrderManager(models.Manager):
    def new_or_get(self, request):
        print(request.user)
        if not request.user.is_anonymous:
            qs = self.get_queryset().filter(user=request.user, status='pending')
            if qs.count() == 1:
                new_obj = False
                print('This user already has a pending order')
                order_obj = qs.first()
                items = order_obj.orderitem_set.all()

                session_order_id = request.session.get('order_id', None)
                session_order_qs = self.get_queryset().filter(id=session_order_id)
                if session_order_qs.count() == 1:
                    print('This user also have some items in session')
                    session_order_obj = session_order_qs.first()       # items = order.orderitem_set.all()
                    session_items = session_order_obj.orderitem_set.all()
                    print('items: ', items)
                    for session_item in session_items:
                        for item in items:
                            if item.product.title == session_item.product.title:
                                print('similar items found...')
                                item.quantity = item.quantity + session_item.quantity
                                item.save()

                            else:
                                session_item.order = order_obj
                                session_item.save()
                        # session_items.delete()


                return order_obj, new_obj



        order_id = request.session.get('order_id', None)
        qs = self.get_queryset().filter(id=order_id)
        if qs.count() == 1:
            new_obj = False
            print('Order id already exists')
            order_obj = qs.first()
            if request.user.is_authenticated and order_obj.user is None:
                order_obj.user = request.user
                order_obj.save()
        else:
            order_obj = Order.objects.new(user=request.user)
            new_obj = True
            print('New Order created')
            request.session['order_id'] = order_obj.id
        return order_obj, new_obj


    def new(self, user=None):
        user_obj = None
        # qs = self.model.objects.filter()
        if user is not None:
            if user.is_authenticated:
                user_obj = user     
        return self.model.objects.create(user=user_obj)


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
