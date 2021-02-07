from django.db import models

from cart.models import Customer

class Address(models.Model):
    customer            = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    city                 = models.CharField(max_length=220)
    full_address         = models.CharField(max_length=220)
    receiver_name        = models.CharField(max_length=220)

    def __str__(self):
        return f'{self.receiver_name} form {self.city}'