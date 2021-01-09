from django.db import models


class Category(models.Model):
    name                = models.CharField(max_length=120)
    parent              = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    nesting_level       = models.PositiveIntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name