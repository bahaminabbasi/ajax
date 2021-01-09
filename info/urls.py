from django.urls import path

from .views import *

app_name = 'info'

urlpatterns = [
    path('', info_home, name='info-home'),
]
