# users/urls.py
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    url(r'^api/(?P<pk>[0-9]+)/', views.UserDetailView.as_view(), name='detailview'),
    url(r'^api/', views.UserListView.as_view(), name='listview'),
    url(r'^login/', views.CustomLoginView.as_view(), name='login'),
    url(r'^signup/', views.SignUpView.as_view(), name='signup'),
    url(r'^edit/(?P<pk>[0-9]+)/', login_required(views.EditView.as_view()), name='edit'),
]