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
