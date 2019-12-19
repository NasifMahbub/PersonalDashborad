# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        image= forms.ImageField(label = 'Choose your image',  help_text = 'The image should be cool.')
        fields = ('username', 'first_name', 'last_name', 'email', 'contact_no', 'image')

class CustomUserChangeForm(UserChangeForm, forms.ModelForm):

    class Meta:
        model = CustomUser
        image= forms.ImageField(label = 'Choose your image',  help_text = 'The image should be cool.')
        fields = ('username', 'first_name', 'last_name', 'email', 'contact_no', 'password', 'image')