from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required , user_passes_test
from .forms import UserRegisterForm
from .models import Profile

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('users-login')
    else:
        form = UserRegisterForm()
    return render(request , 'users/register.html' , {'RegisterForm':form})



