from django.shortcuts import render

# Create your views here.

def pet_profile(request):
    return render(request, 'pets/pet_profile.html')

def pet_page(request):
    return render(request, 'pets/adoptme.html')

def application(request):
    return render(request, 'pets/application.html')