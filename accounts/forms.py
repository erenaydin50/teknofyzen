from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email Adresi')
    password1 = forms.CharField(
        label='Şifre',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Şifre (Tekrar)',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        labels = {
            'username': 'Kullanıcı Adı',
            'email': 'Email Adresi',
        }