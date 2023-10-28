from django.shortcuts import render, redirect
from .models import Cart, CartItem, Product, User
from products.models import ProductCategory
from django.contrib.auth.decorators import login_required


@login_required(login_url='/users/login/')
def cart(request):
    categories = ProductCategory.objects.all()

    if request.user.is_authenticated:
        user = request.user
        user = User.objects.get(username=user)
        cart, created = Cart.objects.get_or_create(user=user)
        items = cart.cartitem_set.all()
    else:
        items = []
        cart = {'get_cart_total': 0, 'get_cart_item': 0}
    context = {
        'title': 'Корзина',
        'items': items,
        'cart': cart,
        'categories': categories
    }
    return render(request, 'carts/cart.html', context)


@login_required(login_url='/users/login/')
def add_to_cart(request, product_id):
    current_page = request.META.get('HTTP_REFERER')
    user = request.user
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=user)
    cart_item, item_created = CartItem.objects.get_or_create(product=product, cart=cart)
    cart_item.quantity += 1
    cart_item.save()
    return redirect(current_page)


@login_required(login_url='/users/login/')
def minus_cart(request, product_id):
    current_page = request.META.get('HTTP_REFERER')
    user = request.user
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get(user=user)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect(current_page)
