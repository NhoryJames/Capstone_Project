from django.urls import path
from . import views

urlpatterns = [
    path('staff/dashboard', views.staff_dashboard, name='staff_dashboard'),
    path('staff/dashboard/applications', views.staff_application_dashboard, name='staff_application_dashboard'),
    path('staff/dashboard/campaigns', views.staff_campaign_dashboard, name='staff_campaign_dashboard'),
    path('staff/dashboard/pets', views.staff_pet_dashboard, name='staff_pet_dashboard'),
    
    path('staff/dashboard/pets/add_pet', views.add_pet, name='add_pet'),
    path('staff/dashboard/pets/edit_pet', views.edit_pet, name='edit_pet'),
    
    path('staff/dashboard/campaigns/add_campaign', views.add_campaign, name='add_campaign'),
    path('staff/dashboard/campaigns/edit_campaign', views.edit_campaign, name='edit_campaign'),

    path('staff/dashboard/applications/review', views.review_application, name='review_application'),
]