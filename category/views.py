from django.shortcuts import render
from django.http import JsonResponse

from .models import Category
from .forms import ProductForm


def category_home(request):
    return render(request, 'category/category_home.html')


def select_category(request):
    form = ProductForm()
    categories = Category.objects.filter(nesting_level=0)
    context = {
        'categories': categories,
        'form': form,
    }
    return render(request, 'category/category_select.html', context)


def levelzero_selected(request):
    if request.method == 'POST':
        selected_category = request.POST['selected_category']
        cat_obj = Category.objects.filter(name=selected_category, nesting_level=0).first()
        levelzero_selected = Category.objects.filter(parent=cat_obj, nesting_level=1)
        result = []
        for levz in levelzero_selected:
            result.append(levz.name)
        return JsonResponse({'result': result})


def levelone_selected(request):
    if request.method == 'POST':
        selected_category_one = request.POST['selected_category_one']
        cat_obj = Category.objects.filter(name=selected_category_one, nesting_level=1).first()
        levelone_selected = Category.objects.filter(parent=cat_obj, nesting_level=2)
        result = []
        for levz in levelone_selected:
            result.append(levz.name)
        return JsonResponse({'result': result})

