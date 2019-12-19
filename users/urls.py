# users/urls.py
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'signup/', views.SignUpView.as_view(), name='signup'),
    url(r'edit/(?P<pk>[0-9]+)/', login_required(views.EditView.as_view()), name='edit'),
]