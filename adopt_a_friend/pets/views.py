from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.

def pet_profile(request, petId, slug):
    pet = get_object_or_404(Pet, petId=petId, slug=slug)
    medical = get_object_or_404(PetMedical, petId=pet)
    images = PetImage.objects.filter(petId=pet)

    context = {
            'pet': pet,
            'medical': medical,
            'images': images,
        }

    return render(request, 'pets/pet_profile.html', context)

def pet_page(request):
    query = request.GET.get('q')
    pets = Pet.objects.all()

    if query:
        # Filter pets based on the search query
        pets = pets.filter(
            Q(petName__icontains=query) |
            Q(animalType__icontains=query) |
            Q(breed__icontains=query)
        )

    pets = pets.order_by('petId')
    
    return render(request, 'pets/adoptme.html', {'pets': pets})

@login_required
def application(request, slug):
    pet = get_object_or_404(Pet, slug=slug)
    user = request.user

    if request.method == 'POST':
        application_form = ApplicationForm(request.POST)
        house_picture_formset = HousePictureFormSet(request.POST, request.FILES, prefix='house_picture')
        id_picture_formset = IdPictureFormSet(request.POST, request.FILES, prefix='id_picture')
        condo_agreement_form = CondoAgreementForm(request.POST, request.FILES)

        if (
            application_form.is_valid()
            and house_picture_formset.is_valid()
            and id_picture_formset.is_valid()
            and condo_agreement_form.is_valid()
        ):
            # Save the main application form
            application_instance = application_form.save(commit=False)
            application_instance.pet = pet
            application_instance.user = user
            application_instance.save()

            # Save the related forms in the formsets
            house_picture_formset.instance = application_instance
            house_picture_formset.save()

            id_picture_formset.instance = application_instance
            id_picture_formset.save()

            # Save the condo agreement form if provided
            if request.FILES.get('condoAgreement'):
                condo_agreement_instance = condo_agreement_form.save(commit=False)
                condo_agreement_instance.applicationId = application_instance
                condo_agreement_instance.save()

            # Redirect to a success page or any other desired page
            return redirect('submitted')  # Replace 'success_page' with the actual URL or name of the success page

    else:
        # Pass the logged-in user to the form
        application_form = ApplicationForm(initial={'adopteeFirstName': user.first_name,
                                                    'adopteeLastName': user.last_name,
                                                    'adopteeHomeAddress': user.home_address,
                                                    'adopteeContactNum': user.contact_num})
        house_picture_formset = HousePictureFormSet(prefix='house_picture')
        id_picture_formset = IdPictureFormSet(prefix='id_picture')
        condo_agreement_form = CondoAgreementForm()

    context = {
        'pet': pet,
        'user': user,
        'application_form': application_form,
        'house_picture_formset': house_picture_formset,
        'id_picture_formset': id_picture_formset,
        'condo_agreement_form': condo_agreement_form,
    }

    return render(request, 'pets/application.html', context)

@login_required
def submitted(request):
    return render(request, 'pets/application_submitted.html')
