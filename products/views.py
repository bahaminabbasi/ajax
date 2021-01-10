from django.shortcuts import render, redirect, HttpResponse
import os

from .models import Product
from category.forms import ProductForm
from category.models import Category
from .filters import ProductFilter


def products_home(request):
    return render(request, 'products/products_home.html')


def list_view(request):
    products = Product.objects.all()
    categories = Category.objects.filter(nesting_level=0)
    if request.method == 'POST':
        print(request.POST)
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'products/list_view.html', context)


def filter_view(request):
    products = Product.objects.all()
    myFilter = ProductFilter(request.GET, queryset=products)
    products = myFilter.qs
    context = {
        'products': products,
        'myFilter': myFilter
    }
    return render(request, 'products/filter_view.html', context)


def sort_filter(request, sort):
    products = Product.objects.all().order_by(sort)
    context = {
        'products': products,
    }
    return render(request, 'products/list_view.html', context)


def products_list(request):
    products = Product.objects.all()
    return render(request, 'products/products_list.html', {'products': products})


def product_edit(request, id):
    product = Product.objects.filter(pk=id).first()
    cat = product.category
    categories = Category.objects.filter(nesting_level=0)
    context = {
            'product': product,
            'categories': categories,
        }
    if cat is not None:
        if cat.nesting_level == 2:
            cat1 = cat.parent
            cat0 = cat1.parent
            context = {
                'product': product,
                'categories': categories,
                'cat2': cat,
                'cat1': cat1,
                'cat0': cat0,
            }
        elif cat.nesting_level == 1:
            cat0 = cat.parent
            context = {
                'product': product,
                'categories': categories,
                'cat1': cat,
                'cat0': cat0
            }
        else:
            context = {
                'product': product,
                'categories': categories,
                'cat0': cat,
            }
    if request.method == 'POST':
        title = request.POST['title']
        brand = request.POST['brand_name']
        # cat check
        if request.POST['select_categories'] == '-------------':
            edited_cat = cat
        else:
            if request.POST['leveltwo_placeholder'] != '-------------':
                mod_cat = request.POST['leveltwo_placeholder']
                edited_cat = Category.objects.filter(name=mod_cat).first()
            elif request.POST['levelone_placeholder'] != '-------------':
                mod_cat = request.POST['levelone_placeholder']
                edited_cat = Category.objects.filter(name=mod_cat).first()
            else:
                mod_cat = request.POST['select_categories']
                edited_cat = Category.objects.filter(name=mod_cat).first()
        # image check
        if 'image' in request.POST:
            print('no new image')
            image = product.image
        else:
            os.remove(product.image.path)
            image = request.FILES['image']
        b = Product(title=title, brand_name=brand, image=image, category=edited_cat)
        b.save()
        product.delete()
        return redirect('products:product-lists')     
    return render(request, 'products/product_edit.html', context)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            image = form.cleaned_data['image']
            cat0 = request.POST['select_categories']
            cat1 = request.POST['levelone_placeholder']
            cat2 = request.POST['leveltwo_placeholder']
            cat = Category.objects.filter(name=cat2).first()
            b = Product(title=title, image=image, category=cat)
            b.save()
            return redirect('main:home')
            
    return render(request, 'products/add_product.html')


def delete_product(request, id):
    product = Product.objects.filter(pk=id).first()
    os.remove(product.image.path)
    product.delete()
    return redirect('products:product-lists')


def product_detail(request, slug):
   
    qs = Product.objects.filter(slug=slug)
    if qs.exists():
        product = qs.first()
    else:
        return HttpResponse('not found')
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)