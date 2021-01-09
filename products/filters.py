import django_filters
from django.db import models
from django import forms

from .models import Product
from category.models import Category



class ProductFilter(django_filters.FilterSet): 
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    class Meta:
        model = Product
        fields = ['category', 'brand_name']



# iquery = LiveDataFeed.objects.values_list('unit_id', flat=True).distinct()
#     iquery_choices = [('', 'None')] + [(id, id) for id in iquery]
#     unit_id = forms.ChoiceField(iquery_choices,
#                                 required=False, widget=forms.Select())

# queryset=Product.objects.all(), 









# class ProductFilter(django_filters.FilterSet):
#     # price = django_filters.NumberFilter()
#     # price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
#     # price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
#     # location = django_filters.ModelChoiceFilter(queryset=Location.objects.all(), widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
#     brand_name = django_filters.ModelMultipleChoiceFilter(
#                     queryset=Product.objects.values_list('brand_name', flat=True).distinct(),
#                     widget=forms.CheckboxSelectMultiple())  
#     # price_range = DateFromToRangeFilter(widget=RangeWidget(attrs={'placeholder': 'YYYY/MM/DD'}))
#     # p = django_filters.MultipleChoiceField
#     class Meta:
#         model = Product
#         fields = ['brand_name']
#     #     filter_overrides = {
#     #         models.CharField: {
#     #             'filter_class': django_filters.CharFilter,
#     #             'extra': lambda f: {
#     #                 'lookup_expr': 'icontains',
#     #                 'widget': forms.CheckboxSelectMultiple,
#     #             },
#     #         },
#     #     }


# # class PriceFilter(django_filters.FilterSet):
# #     STATUS_CHOICES = (
# #         (0, _('Pending')),
# #         (1, _('Approved')),
# #         (2, _('Deleted')),
# #     )

# #     location = django_filters.ModelChoiceFilter(queryset=Location.objects.all(), widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
# #     item = django_filters.ModelChoiceFilter(queryset=Item.objects.all(), widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
# #     user = django_filters.ModelChoiceFilter(queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
# #     status = django_filters.ChoiceFilter(choices=STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
# #     date = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'class': 'datepicker form-control form-control-sm', 'placeholder': 'YYYY-MM-DD'}))
# #     class Meta:
# #         model = Price
# #         fields = ('location', 'item', 'unit', 'date', 'status', 'user', 'approved', )
# #     forms.MultipleChoiceField(
# #     required=False,
# #     widget=forms.CheckboxSelectMultiple,
# #     choices=FAVORITE_COLORS_CHOICES,
# # )