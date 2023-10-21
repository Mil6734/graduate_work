from django import forms

from .models import ShippingAddress


class OrderForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ('first_name', 'last_name', 'email', 'address', 'phone', 'zipcode')

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'fa fa-user', 'placeholder': 'Иван'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'fa fa-user', 'placeholder': 'Иванов'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'fa fa-envelope', 'placeholder': 'you@gmail.com'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'fa fa-address-card-o', 'placeholder': 'Россия, Москва'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'fa fa-institution', 'placeholder': '79517031177'}))
    zipcode = forms.CharField(widget=forms.TextInput(attrs={'class': 'fa fa-institution', 'placeholder': '211000'}))
