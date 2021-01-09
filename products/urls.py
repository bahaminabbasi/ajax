from django.urls import path
from .views import *
# from views import *

app_name = 'products'

urlpatterns = [
    path('', products_home, name='prodcuts-home'),
    path('addproduct/', add_product, name='add-product'),
    path('list/', products_list, name='product-lists'),
    path('edit/<int:id>', product_edit, name='product-edit'),
    path('delete/<int:id>', delete_product, name='product-delete'),
    path('listview/', list_view, name='list-view'),
    path('sortfilter/<str:sort>', sort_filter, name='sort-filter'),
    path('filterview/', filter_view, name='filter-view'),
    path('detail/<slug:slug>', product_detail, name='detail'),
]
