from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.create_user, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout, name='logout'),
    ]