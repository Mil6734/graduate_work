from django.shortcuts import render, redirect
from .models import Cart, CartItem, Product, User


def cart(request):
    if request.user.is_authenticated:
        username = request.user.username
        user = User.objects.get(username=username)
        cart, created = Cart.objects.get_or_create(username=user)
        items = cart.cartitem_set.all()
    else:
        items = []
        cart = {'get_cart_total': 0, 'get_cart_item': 0}
    context = {
        'title': 'Корзина',
        'items': items,
        'cart': cart,
    }
    return render(request, 'carts/cart.html', context)


def add_to_cart(request, product_id):
    current_page = request.META.get('HTTP_REFERER')
    user = request.user
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(username=user)
    cart_item, item_created = CartItem.objects.get_or_create(product=product, cart=cart)
    cart_item.quantity += 1
    cart_item.save()
    return redirect(current_page)


def minus_cart(request, product_id):
    current_page = request.META.get('HTTP_REFERER')
    user = request.user
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get(username=user)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect(current_page)


def remove_cart(request, cart_item_id):
    user = request.user
    cart_item = CartItem.objects.get(id=cart_item_id, cart__username=user)
    cart_item.delete()
    return redirect('cart')
