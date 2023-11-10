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
        pet_form = PetForm(request.POST)
        pet_medical_form = PetMedicalForm(request.POST)

        if pet_form.is_valid() and pet_medical_form.is_valid():
            pet_instance = pet_form.save()
            petmedical = pet_medical_form.save(commit=False)
            petmedical.petId = pet_instance
            petmedical.save()
            return redirect('staff_pet_dashboard')

    else:
        pet_form = PetForm()
        pet_medical_form = PetMedicalForm()
    
    return render(request, 'staff/add_pet.html', {'pet_form': pet_form, 'pet_medical_form': pet_medical_form})

def edit_pet(request):
    return render(request, 'staff/edit_pet.html')

def add_campaign(request):
    return render(request, 'staff/add_campaign.html')

def edit_campaign(request):
    return render(request, 'staff/edit_campaign.html')

def review_application(request):
    return render(request, 'staff/review_application.html')

