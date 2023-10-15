from django import forms
from .models import Users
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your email',
        'class': 'w-full px-6 py-3 mb-2 border border-slate-600 rounded-lg font-medium'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full px-6 py-3 mb-2 border border-slate-600 rounded-lg font-medium'
    }))

    
    