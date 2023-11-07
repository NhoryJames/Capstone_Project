from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from adopt_a_friend import settings

urlpatterns = [
    path('signup/', views.create_user, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/',  LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('profile/<slug:slug>', views.profile, name='profile'),
    path('sent_email/', views.sent_email, name='sent_email'),
    ]