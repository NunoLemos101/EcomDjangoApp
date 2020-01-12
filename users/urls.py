from django.contrib import admin
from django.urls import path
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .forms import UserRegisterForm

urlpatterns = [
    path('login/' , auth_views.LoginView.as_view(template_name='users/login.html') , name='users-login'),
    path('register/' , user_views.register , name='users-register'),
    path('logout/' , auth_views.LogoutView.as_view(template_name='users/logout.html') , name='users-logout'),
]
