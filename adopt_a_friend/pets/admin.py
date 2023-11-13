from django.contrib import admin
from .models import Pet, PetMedical, PetImage

# Register your models here.

admin.site.register(Pet)
admin.site.register(PetMedical)
admin.site.register(PetImage)