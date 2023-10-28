from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User, EmailVerify
from django import forms

import uuid
from datetime import timedelta
from django.utils.timezone import now


class UserLogin(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Введите логин'}))
    password = forms.CharField(
        widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control form-control-sm', 'placeholder': 'Введите пароль'})


class UserRegister(UserCreationForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите адрес электронной почты'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите логин'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = "form-control form-control-sm"

    def save(self, commit=True):
        user = super().save(commit=True)
        expiration = now() + timedelta(hours=3)
        record = EmailVerify.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
        record.send_verification_email()
        return user
