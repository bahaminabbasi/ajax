"""A URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('address/', include('address.urls', namespace='address')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('category/', include('category.urls', namespace='category')),

    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),

    path('info/', include('info.urls', namespace='info')),
    path('invoice/', include('invoice.urls', namespace='invoice')),
    path('', include('main.urls', namespace='main')),
    path('products/', include('products.urls', namespace='products')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if not settings.DEBUG:
    urlpatterns += url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})
    urlpatterns += url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT})


# url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
# url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
