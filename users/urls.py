# users/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'signup/', views.SignUpView.as_view(), name='signup'),
    url(r'edit/(?P<pk>[0-9]+)/', views.EditView.as_view(), name='edit'),
]