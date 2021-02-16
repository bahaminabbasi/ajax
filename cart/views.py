from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import *
from address.models import Address


def cart(request):

    order, created  = Order.objects.new_or_get(request)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    # # context = {'cart': cart_obj}
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
    if request.user.is_authenticated:
        user = request.user
        address = Address.objects.filter(user=user).first()
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.orderitem_set.all() # gets all the orderitems that hava 'order' as their parent ; return a qs
        # print(items.last().product.title)
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items': items, 'order': order, 'user': user, 'address': address}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    if request.method == 'POST':
        productId = request.POST['productId']
        action = request.POST['action']
        print(productId, action)

        max_reached = 'no'
        # user = request.user
        product = Product.objects.get(id=productId)

        quantity = product.quantity

        order, created = Order.objects.new_or_get(request)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

        orderitem_quantity = orderItem.quantity

        if action == 'add' and orderitem_quantity < quantity:
            orderItem.quantity = (orderItem.quantity + 1)
        elif action == 'add' and orderitem_quantity >= quantity:
            max_reached = 'yes'
        elif action == 'remove':
            orderItem.quantity = (orderItem.quantity - 1)

        orderItem.save()

        if orderItem.quantity <= 0:
            orderItem.delete()

        
        

    return JsonResponse({'max_reached': max_reached})

def remove_item(request, id):
    orderItem = OrderItem.objects.filter(id=id).first()
    orderItem.delete()
    return redirect('cart:cart')