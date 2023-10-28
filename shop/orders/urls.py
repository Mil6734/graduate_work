from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('create-order/', views.create_order, name='create_order'),
    path('thank-you/<int:order_id>/', views.thank_you, name='thank_you'),
]