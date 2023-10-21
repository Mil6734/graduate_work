from django.shortcuts import render, redirect
from .forms import OrderForm
from carts.models import Cart, CartItem


def checkout(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order_form = form.save(commit=False)
            order_form.username = request.user
            order_form.save()

            return redirect('cart')
    else:
        form = OrderForm()
    context = {
        'form': form,
        'title': 'Оформление заказа',
    }

    return render(request, 'orders/checkout.html', context)
