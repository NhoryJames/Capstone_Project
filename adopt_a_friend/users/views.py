from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout
from .forms import UsersForm, LoginForm
from verify_email.email_handler import send_verification_email

# Create your views here.

def create_user(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            # Save the user object
            inactive_user = send_verification_email(request, form)
            user = form.save()
            # Redirect to a success page or do something else
            return redirect('success_page')
    else:
        form = UsersForm()

    return render(request, 'users/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('/home/')
    else:
        form = LoginForm()

    return render(request, 'main/login.html', {'form': form})

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/home/')  # Replace 'home' with the URL where you want to redirect after logout.