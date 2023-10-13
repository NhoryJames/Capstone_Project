from django.contrib import admin
from .models import PreferenceTbl, BreedPreferenceTbl, PersonalityPreferenceTbl, ColorPreferenceTbl

admin.site.register(PreferenceTbl)
admin.site.register(BreedPreferenceTbl)
admin.site.register(PersonalityPreferenceTbl)
admin.site.register(ColorPreferenceTbl)
# Register your models here.
