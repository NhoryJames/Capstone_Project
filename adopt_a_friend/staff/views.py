from django.shortcuts import render, redirect
from .forms import *
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from pets.models import *
from donation.models import *
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .decorators import staff_required

# Create your views here.

@staff_required
def staff_dashboard(request):
    return render(request, 'staff/staff_dashboard.html')

@staff_required
def staff_application_dashboard(request):
    application = Application.objects.all()
    total_application_count = application.count()
    query = request.GET.get('q')

    if query:
        # Filter campaigns based on the search query
        application = application.filter(
            Q(campaignName__icontains=query) |
            Q(campaignId__icontains=query)
            # Add more fields as needed
            )
    
    return render(request, 'staff/staff_application_dashboard.html', {
        'application':application,
        'total_application_count': total_application_count})

@staff_required
def staff_campaign_dashboard(request):
    fundrasing_campaigns = FundraisingCampaign.objects.all()
    total_campaign_count = fundrasing_campaigns.count()
    query = request.GET.get('q')

    if query:
        # Filter campaigns based on the search query
        fundrasing_campaigns = fundrasing_campaigns.filter(
            Q(campaignName__icontains=query) |
            Q(campaignId__icontains=query)
            # Add more fields as needed
            )

    fundrasing_campaigns  = fundrasing_campaigns.order_by('campaignId')
    items_per_page = 8
    paginator = Paginator(fundrasing_campaigns, items_per_page)
    page = request.GET.get('page')

    try:
        fundrasing_campaigns = paginator.page(page)
    except PageNotAnInteger:
        fundrasing_campaigns = paginator.page(1)
    except EmptyPage:
        fundrasing_campaigns = paginator.page(paginator.num_pages)

    return render(request, 'staff/staff_campaign_dashboard.html', {
        'fundrasing_campaigns':fundrasing_campaigns,
        'total_campaign_count': total_campaign_count})

@staff_required
def staff_pet_dashboard(request):
    query = request.GET.get('q')

    # Retrieve all pets
    pets = Pet.objects.all()

    if query:
        # Filter pets based on the search query
        pets = pets.filter(
            Q(petName__icontains=query) |
            Q(animalType__icontains=query) |
            Q(breed__icontains=query)
        )

    pets = pets.order_by('petId')
    total_pets_count = pets.count()
    items_per_page = 8
    paginator = Paginator(pets, items_per_page)
    page = request.GET.get('page')

    try:
        pets = paginator.page(page)
    except PageNotAnInteger:
        pets = paginator.page(1)
    except EmptyPage:
        pets = paginator.page(paginator.num_pages)

    return render(request, 'staff/staff_pet_dashboard.html', {'pets': pets, 'total_pets_count': total_pets_count})

@staff_required
def add_pet(request):
    if request.method == 'POST':
        pet_form = PetForm(request.POST)
        pet_medical_form = PetMedicalForm(request.POST)
        pet_image_formset = PetImageFormset(request.POST, request.FILES)

        if pet_form.is_valid() and pet_medical_form.is_valid() and pet_image_formset.is_valid():
            pet_instance = pet_form.save()
            
            petmedical = pet_medical_form.save(commit=False)
            petmedical.petId = pet_instance
            petmedical.save()

            for pet_image_form in pet_image_formset:
                pet_image = pet_image_form.save(commit=False)
                pet_image.petId = pet_instance
                pet_image.save()

            return redirect('staff_pet_dashboard')

    else:
        pet_form = PetForm()
        pet_medical_form = PetMedicalForm()
        pet_image_formset = PetImageFormset()
    
    return render(request, 'staff/add_pet.html', 
                  {'pet_form': pet_form, 
                   'pet_medical_form': pet_medical_form,
                   'pet_image_formset': pet_image_formset})

@staff_required
def edit_pet(request, slug):
    pet = get_object_or_404(Pet, slug=slug)
    
    if request.method == 'POST':
        pet_form = PetForm(request.POST, instance=pet)
        medical_form = PetMedicalForm(request.POST, instance=pet.petmedical)
        ImageFormset = PetImageFormset(request.POST, request.FILES, instance=pet)

        if pet_form.is_valid() and medical_form.is_valid() and ImageFormset.is_valid():
            pet_form.save()
            medical_form.save()
            ImageFormset.save()

            # Redirect to the same page or another page as needed
            return redirect('staff_pet_dashboard')
    else:
        pet_form = PetForm(instance=pet)
        medical_form = PetMedicalForm(instance=pet.petmedical)
        ImageFormset = PetImageFormset(instance=pet)

    return render(request, 'staff/edit_pet.html', {
        'pet': pet,
        'pet_form': pet_form,
        'medical_form': medical_form,
        'ImageFormset': ImageFormset,
    })

@staff_required
def delete_pet(request, pet_id):
    pet = get_object_or_404(Pet, petId=pet_id)

    if request.method == 'DELETE':
        try:
            pet.delete()
            return JsonResponse({'message': 'Pet deleted successfully.'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'message': 'Invalid request method.'}, status=400)

@staff_required
def add_campaign(request):
    if request.method == 'POST':
        form = CampaignForm(request.POST, request.FILES)
        if form.is_valid():
            campaign = form.save()
            # Do any additional processing or redirect as needed
            return redirect('staff_campaign_dashboard')  # Redirect to campaign detail page
    else:
        form = CampaignForm()
    return render(request, 'staff/add_campaign.html', {'form': form})

@staff_required
def edit_campaign(request, campaign_id):
    campaign = get_object_or_404(FundraisingCampaign, campaignId=campaign_id)

    if request.method == 'POST':
        form = CampaignForm(request.POST, instance=campaign)
        if form.is_valid():
            form.save()
            return redirect('staff_campaign_dashboard')
    else:
        form = CampaignForm(instance=campaign)

    return render(request, 'staff/edit_campaign.html', {'form': form, 'campaign':campaign})

@staff_required
def delete_campaign(request, campaign_id):
    campaign = get_object_or_404(FundraisingCampaign, campaignId=campaign_id)

    if request.method == 'DELETE':
        try:
            campaign.delete()
            return JsonResponse({'message': 'Campaign deleted successfully.'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'message': 'Invalid request method.'}, status=400)

@staff_required
def review_application(request):
    
    return render(request, 'staff/review_application.html')

