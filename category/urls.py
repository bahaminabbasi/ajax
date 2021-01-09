from django.urls import path
from .views import *

app_name = 'category'

urlpatterns = [
    path('', category_home, name='category-home'),
    path('select/', select_category, name='category-select'),

    # AJAX ONLY
    path('levelzero_selected/', levelzero_selected, name='levelzero-selected'),
    path('levelone_selected/', levelone_selected, name='levelone-selected'),
]
