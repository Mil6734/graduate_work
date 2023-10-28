from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('verify/<str:email>/<uuid:code>/', views.email_verify, name='email_verify'),
    path('profile/user-orders', views.user_orders, name='user_orders'),
]