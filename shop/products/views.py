from django.shortcuts import render
from .models import *


def home(request):
    context = {
        'title': 'Главная'
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
    context = {
        "title": product_obj.name,
        'product': product_obj,
        # 'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/product.html', context)


def cart(request):
    context = {
        'title': 'Корзина'
    }
    return render(request, 'products/cart.html', context)


def checkout(request):
    context = {
        'title': 'Привет'
    }
    return render(request, 'products/checkout.html', context)