from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth import login as auth_login, logout
from .forms import UsersForm, LoginForm, ProfilePictureUpdateForm, UserUpdateForm, PreferenceForm
from verify_email.email_handler import send_verification_email
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from django.contrib import messages
from django.urls import reverse
import os
from django.conf import settings

# Create your views here.

@unauthenticated_user
def create_user(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        preference_form = PreferenceForm(request.POST)

        if form.is_valid() and preference_form.is_valid():
            inactive_user = send_verification_email(request, form)
            user = form.save()
            
            preference = preference_form.save(commit=False)
            preference.adopter = user
            preference.save()

            return redirect('/sent_email/')
    else:
        form = UsersForm()
        preference_form = PreferenceForm()

    return render(request, 'users/signup.html', {
        'form': form, 
        'preference_form': preference_form, 
        })

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
def profile(request, slug, id):
    user = get_object_or_404(Users, slug=slug)
    adopters = Users.objects.get(pk=id)
    preference = Preference.objects.get(adopter=adopters)

    context = {
        'user': user,
        'preference': preference,
    }

    return render(request, 'users/profile.html', context)

@login_required
def update_profile(request, slug):
    user = get_object_or_404(Users, slug=slug)
    
    if request.method == 'POST':
        update_user_form = UserUpdateForm(request.POST, instance=request.user)
        update_profile_form = ProfilePictureUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if update_user_form.is_valid() and update_profile_form.is_valid():
            # Delete the previous profile picture if it exists
            previous_picture = user.profile.image
            if previous_picture:
                full_path = os.path.join(settings.MEDIA_ROOT, str(previous_picture))
                if os.path.exists(full_path):
                    os.remove(full_path)

            update_user_form.save()
            update_profile_form.save()
            
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile', slug=user.slug)  # Assuming 'profile' is the URL name for the user's profile page
        
    else:
        update_user_form = UserUpdateForm(instance=request.user)
        update_profile_form = ProfilePictureUpdateForm(instance=request.user.profile)
    
    context = {
        'update_user_form': update_user_form,
        'update_profile_form': update_profile_form,
        'user': user,
    }

    return render(request, 'users/update_profile.html', context)
