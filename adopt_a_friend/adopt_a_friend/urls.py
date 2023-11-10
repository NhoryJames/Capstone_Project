from django.contrib import admin
from django.urls import path, include
from main.views import *
from users.views import *
from pets.views import *
from staff.views import *
from donation.views import *

urlpatterns = [
    path('', index, name='index'),
    path('donation/', donation, name='donation'),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', include('videochat.urls')),
    path('verification/', include('verify_email.urls')),	
    path('', include("users.urls")),
    path('', include("pets.urls")),
    path('', include("staff.urls")),
    path('', include("donation.urls")),
]
