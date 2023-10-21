from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('cart/add-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/minus-cart/<int:product_id>/', views.minus_cart, name='minus_cart'),
    path('cart/remove-cart/<int:cart_item_id>/', views.remove_cart, name='remove_cart'),


]