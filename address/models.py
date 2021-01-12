from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    user_name            = models.ForeignKey(User, on_delete=models.CASCADE)
    city                 = models.CharField(max_length=220)
    full_address         = models.CharField(max_length=220)
    receiver_name        = models.CharField(max_length=220)

    def __str__(self):
        return f'{self.receiver_name} form {self.city}'