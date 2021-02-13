## First Version
class OrderManager(models.Manager):
    def new_or_get(self, request):
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
        if user is not None:
            if user.is_authenticated:
                user_obj = user     
        return self.model.objects.create(user=user_obj)

## Second Version [problem is that it adds session cart items to db cart items
# every time, instead it should add it once and del session cart]

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