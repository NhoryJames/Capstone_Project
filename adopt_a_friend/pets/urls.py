from django.urls import path
from . import views

urlpatterns = [
    path('pet_profile/', views.pet_profile, name='pet_profile'),
    path('adoptme/', views.pet_page, name='pet_page')
]