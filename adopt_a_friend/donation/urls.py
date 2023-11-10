from django.urls import path
from . import views

urlpatterns = [
    path('donate/', views.donation_profile, name='donation_profile'),
    path('donation_page/', views.donation_page, name='donation_page'),
    path('donate/payment/', views.payment, name='payment'),
]