from django.shortcuts import render

# Create your views here.

def reco(response):
    return render(response, "recommendation/reco.html")
