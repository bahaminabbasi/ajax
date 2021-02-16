from django.db import models
from django.contrib.auth.models import User

from cart.models import Order
from address.models import Address



class Invoice(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('canceled', 'Canceled'),
        ('paid', 'Paid'),
    )
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    address         = models.OneToOneField(Address, null=True, blank=True, on_delete=models.SET_NULL)
    order           = models.ForeignKey(Order, on_delete=models.CASCADE)
    status          = models.CharField(max_length=20, choices=STATUS, default='pending')
    date            = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} from {self.address.city} order_id:{self.order.id}/{self.status}'
