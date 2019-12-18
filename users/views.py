# users/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from django.views import generic
from .models import CustomUser

from .forms import CustomUserCreationForm, CustomUserChangeForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class EditView(UpdateView):
    model = CustomUser
    form = CustomUserChangeForm
    success_url = reverse_lazy('home')
    template_name = 'edit.html'
    fields = ('username', 'first_name', 'last_name', 'email', 'contact_no')