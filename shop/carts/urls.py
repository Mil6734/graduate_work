from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('cart/add-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/minus-cart/<int:product_id>/', views.minus_cart, name='minus_cart'),
]
