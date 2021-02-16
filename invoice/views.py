from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Invoice
from cart.models import Order
from address.models import Address


@login_required
def invoice_detail(request, order_id):
    invoice = get_object_or_404(Invoice, id=order_id)
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'invoice/invoice.html', {'order': order})


@login_required
def invoice_create(request):
    print(request.POST)
    if request.method == 'POST':
        print('POOSTT')
        user = request.user
        address = Address.objects.filter(user=user).first()
        order_obj, order_created = Order.objects.get_or_create(user=user)
        items = order_obj.orderitem_set.all()

        invoice_obj, invoice_created = Invoice.objects.get_or_create(
                                                            user=user,
                                                            address=address,
                                                            order=order_obj,
                                                            )

    
        context = {
            'invoice': invoice_obj,
            'items': items,
            'order': order_obj,
        }
    else:
        print('NOOOO')
        context = {}
    return render(request, 'invoice/invoice.html', context)

