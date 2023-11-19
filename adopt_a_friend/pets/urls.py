from django.urls import path, include
from . import views

urlpatterns = [
    path('pet_profile/<str:slug>-<str:petId>/', views.pet_profile, name='pet_profile'),
    path('adoptme/', views.pet_page, name='pet_page'),
    path('application/<str:slug>/', views.application, name='application'),
    path('submitted/', views.submitted, name='submitted'),
]