from django.shortcuts import render, redirect, get_object_or_404
from .models import Users
from django.contrib.auth import login as auth_login, logout
from .forms import UsersForm, LoginForm
from verify_email.email_handler import send_verification_email
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
# Create your views here.

@unauthenticated_user
def create_user(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            # Save the user object
            inactive_user = send_verification_email(request, form)
            user = form.save()
            # Redirect to a success page or do something else
            return redirect('/sent_email/')
    else:
        form = UsersForm()

    return render(request, 'users/signup.html', {'form': form})

@unauthenticated_user
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('index')
    else:
        form = LoginForm()

    return render(request, 'main/login.html', {'form': form})

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)

def sent_email(request):
    return render(request, 'users/sent_email.html')

@login_required
def profile(request, slug):
    user = get_object_or_404(Users, slug=slug)
    return render(request, 'users/profile.html', {'user': user})