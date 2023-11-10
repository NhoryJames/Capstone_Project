from django.shortcuts import render, redirect, get_object_or_404
from .models import Users
from django.contrib.auth import login as auth_login, logout
from .forms import UsersForm, LoginForm, ProfilePictureUpdateForm, UserUpdateForm, PreferenceForm, PersonalityPreferenceFormSet
from verify_email.email_handler import send_verification_email
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from django.contrib import messages
from django.urls import reverse

# Create your views here.

@unauthenticated_user
def create_user(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        preference_form = PreferenceForm(request.POST)
        personality_preference_formset = PersonalityPreferenceFormSet(request.POST)

        if form.is_valid() and preference_form.is_valid() and personality_preference_formset.is_valid():
            inactive_user = send_verification_email(request, form)
            user = form.save()
            
            preference = preference_form.save(commit=False)
            preference.adopter = user
            preference.save()

            for personality_preference_form in personality_preference_formset:
                personality_preference = personality_preference_form.save(commit=False)
                personality_preference.preferenceId = preference
                personality_preference.save()

            return redirect('/sent_email/')
    else:
        form = UsersForm()
        preference_form = PreferenceForm()
        personality_preference_formset = PersonalityPreferenceFormSet()

    return render(request, 'users/signup.html', {
        'form': form, 
        'preference_form': preference_form, 
        'personality_preference_formset': personality_preference_formset
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
def profile(request, slug):
    user = get_object_or_404(Users, slug=slug)
    return render(request, 'users/profile.html', {'user': user})

@login_required
def update_profile(request, slug):
    user = get_object_or_404(Users, slug=slug)
    
    if request.method =='POST':
        update_user = UserUpdateForm(request.POST, 
                                     instance=request.user)
        update_profile = ProfilePictureUpdateForm(request.POST, 
                                                  request.FILES, 
                                                  instance=request.user.profile)
        
        if update_user.is_valid() and update_profile.is_valid():
            update_user.save()
            update_profile.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile', slug=user.slug)
        
    else:
        update_user = UserUpdateForm(instance=request.user)
        update_profile = ProfilePictureUpdateForm(instance=request.user.profile)
    

    context = {
        'update_user': update_user,
        'update_profile': update_profile,
        'user': user
    }

    return render(request, 'users/update_profile.html', context)