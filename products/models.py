from django.db import models

from category.models import Category


class Product(models.Model):
    title               = models.CharField(max_length=200)
    brand_name          = models.CharField(max_length=200, default='new brand')
    price               = models.DecimalField(decimal_places=0, max_digits=30, default=100000)
    quantity            = models.PositiveIntegerField(default='1')
    active              = models.BooleanField(default=True)
    image               = models.ImageField(upload_to='products_pics', null=True, blank=True)
    category            = models.ForeignKey(Category, models.SET_NULL, null=True, blank=True)
    slug                = models.SlugField(max_length=250, blank=True, null=True)
    
    def __str__(self):
        return self.title


    # Handles products that have no image
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = '' # can be placeholder ? !
        return url