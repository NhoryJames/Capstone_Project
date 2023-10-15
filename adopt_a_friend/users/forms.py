from django import forms
from .models import Users
from django.contrib.auth.forms import UserCreationForm

class UsersForm(UserCreationForm):
    class Meta:
        model = Users
        fields = (
            'email', 
            'first_name', 
            'last_name', 
            'age', 
            'gender', 
            'date_of_birth', 
            'home_address', 
            'contact_num'
        )