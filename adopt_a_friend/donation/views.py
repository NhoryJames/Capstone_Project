from django.shortcuts import render

# Create your views here.

def donation_page(request):
    return render(request, 'donation/donation_page.html')

def donation_profile(request):
    return render(request, 'donation/donation_profile.html')

def payment(request):
    return render(request, 'donation/payment.html')

def payment(request):
    return render(request, 'donation/crowdfunding_page.html')