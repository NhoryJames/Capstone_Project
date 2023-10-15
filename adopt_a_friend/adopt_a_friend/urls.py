from django.contrib import admin
from django.urls import path, include
from main.views import *
from users.views import *

urlpatterns = [
    path('home/', index, name='index'),
    path('application/', application, name='application'),
    path('donation/', donation, name='donation'),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', include('videochat.urls')),
    path('verification/', include('verify_email.urls')),	
    path('', include("users.urls")),
]
