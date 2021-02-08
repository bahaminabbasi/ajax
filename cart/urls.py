from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),

    # JS:
    path('update_item/', views.updateItem, name='update-item'),
]