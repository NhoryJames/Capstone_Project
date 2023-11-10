from django.contrib import admin
from .models import Pet, PetMedical

# Register your models here.

admin.site.register(Pet)
admin.site.register(PetMedical)