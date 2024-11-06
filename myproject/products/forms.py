from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product


class UserRegistrationForm(UserCreationForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    # password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']
