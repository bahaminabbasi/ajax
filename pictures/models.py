from django.db import models

from products.models import Product


class Picture(models.Model):
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    pic         = models.ImageField(upload_to='pictures')
    is_main     = models.BooleanField()

    def __str__(self):
        return self.product.title
