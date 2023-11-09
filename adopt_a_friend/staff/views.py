from django.shortcuts import render, redirect
from .forms import *

# Create your views here.

def staff_dashboard(request):
    return render(request, 'staff/staff_dashboard.html')

def staff_application_dashboard(request):
    return render(request, 'staff/staff_application_dashboard.html')

def staff_campaign_dashboard(request):
    return render(request, 'staff/staff_campaign_dashboard.html')

def staff_pet_dashboard(request):
    return render(request, 'staff/staff_pet_dashboard.html')

def add_pet(request):
    if request.method == 'POST':
        form = AddPetForm(request.POST)
        if form.is_valid():
            Pet = form.save()
            return redirect('staff_pet_dashboard')
    else:
        form = AddPetForm()

    return render(request, 'staff/add_pet.html', {'form': form})

def edit_pet(request):
    return render(request, 'staff/edit_pet.html')

def add_campaign(request):
    return render(request, 'staff/add_campaign.html')

def edit_campaign(request):
    return render(request, 'staff/edit_campaign.html')

def review_application(request):
    return render(request, 'staff/review_application.html')

