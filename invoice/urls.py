from django.urls import path

from . import views

app_name = 'invoice'

urlpatterns = [
    path('create/', views.invoice_create, name='create'),
    path('<int:order_id>/', views.invoice_detail, name='detail'),
]
