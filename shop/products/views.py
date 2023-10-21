from django.shortcuts import render
from .models import *


def home(request):
    categories = ProductCategory.objects.all()
    context = {
        'title': 'Главная',
        'categories': categories,
    }
    return render(request, 'products/home.html', context)


def products(request, category_id=None):
    categories = ProductCategory.objects.all()
    context = {
        'title': 'Каталог',
        'categories': categories
    }
    if category_id:
        context.update({'products': Product.objects.filter(category_id=category_id)})
    else:
        context.update({'products': Product.objects.all()})

    return render(request, 'products/products.html', context)


def product(request, pk):
    product_obj = Product.objects.get(id=pk)
    categories = ProductCategory.objects.all()
    context = {
        "title": product_obj.name,
        'product': product_obj,
        'categories': categories,
    }
    return render(request, 'products/product.html', context)


