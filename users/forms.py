# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, SQLUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'contact_no', 'image')

    def save(self, commit=True):
            user = super(CustomUserCreationForm, self).save(commit=False)
            user.username = self.cleaned_data['username']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']
            user.contact_no = self.cleaned_data['contact_no']
            user.image = self.cleaned_data['image']

            if commit:
                user.save()

            return user

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'contact_no', 'password', 'image')

    def save(self, commit=True):
            user = super(CustomUserChangeForm, self).save(commit=False)
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']
            user.contact_no = self.cleaned_data['contact_no']
            user.image = self.cleaned_data['image']

            if commit:
                user.save()

            return user