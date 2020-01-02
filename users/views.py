# users/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.views import generic
from .models import CustomUser
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm


from .serializers import CustomUserSerializer
from .permissions import IsAuthenticatedUserOrAdmin
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from rest_framework.parsers import JSONParser

from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework import viewsets


class HomeView(TemplateView):
    template_name='home.html'

class CustomLoginView(LoginView):
    template_name='registration/login.html'

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class EditView(UpdateView):
    model = CustomUser
    template_name = 'edit.html'
    
    success_url = reverse_lazy('home')
    form = CustomUserChangeForm
    fields = ('first_name', 'last_name', 'email', 'contact_no', 'image')




@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('api-auth/login/', request=request, format=format),
    })


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]
   
class UserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthenticatedUserOrAdmin]

class UserEditView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthenticatedUserOrAdmin]

class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

