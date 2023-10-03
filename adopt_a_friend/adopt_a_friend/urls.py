from django.contrib import admin
from django.urls import path, include
from main.views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('application/', application, name='application'),
    path('donation/', donation, name='donation'),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', include('videochat.urls'))
]