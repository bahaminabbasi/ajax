from django.shortcuts import render
from django.http import JsonResponse

from .models import *


def cart(request):

    order, created  = Order.objects.new_or_get(request)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    # context = {'cart': cart_obj}
    return render(request, 'store/cart.html', context)


    # if request.user.is_authenticated:
    #     customer = request.user.customer
    #     order, created = Order.objects.get_or_create(customer=customer, complete=False)
    #     items = order.orderitem_set.all() # gets all the orderitems that have 'order' as their parent ; return a qs
    #     # print(items.last().product.title)
    # else:
    #     items = []
    #     order = {'get_cart_total':0, 'get_cart_items':0}


def checkout(request):
    # if request.user.is_authenticated:
    #     customer = request.user.customer
    #     order, created = Order.objects.get_or_create(customer=customer, complete=False)
    #     items = order.orderitem_set.all() # gets all the orderitems that hava 'order' as their parent ; return a qs
    #     # print(items.last().product.title)
    # else:
    #     items = []
    #     order = {'get_cart_total':0, 'get_cart_items':0}

    # context = {'items': items, 'order': order}
    return render(request, 'store/checkout.html')


def updateItem(request):
    if request.method == 'POST':
        productId = request.POST['productId']
        action = request.POST['action']
        print(productId, action)
        # user = request.user
        product = Product.objects.get(id=productId)

        order, created = Order.objects.new_or_get(request)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

        if action == 'add':
            orderItem.quantity = (orderItem.quantity + 1)
        elif action == 'remove':
            orderItem.quantity = (orderItem.quantity - 1)

        orderItem.save()

        if orderItem.quantity <= 0:
            orderItem.delete()

    return JsonResponse('Item was added', safe=False)