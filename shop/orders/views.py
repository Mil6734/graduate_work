from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
from carts.models import Cart
from .models import Order, OrderItem, ShippingAddress
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='/users/login/')
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    form = OrderForm()
    context = {'cart': cart, 'form': form}
    return render(request, 'orders/checkout.html', context)


@login_required(login_url='/users/login/')
def thank_you(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/thank_you.html', {'order': order})


@login_required(login_url='/users/login/')
def create_order(request):
    cart = get_object_or_404(Cart, user=request.user)

    if cart.cartitem_set.exists() and request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                payment_method=form.cleaned_data['payment_method'],
                user=request.user,
            )

            ShippingAddress.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address'],
                zipcode=form.cleaned_data['zipcode'],
                order=order,
            )

            for cart_item in cart.cartitem_set.all():
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    price=cart_item.product.price
                )

            cart.cartitem_set.all().delete()
            return redirect('thank_you', order_id=order.id)
    else:
        form = OrderForm()
    messages.warning(
        request, 'Форма не была корректно обработана, введите данные еще раз')
    context = {'form': form, 'cart': cart}
    return render(request, 'orders/checkout.html', context)
