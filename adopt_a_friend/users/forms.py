from django import forms
from .models import Users
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UsersForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'w-full px-6 py-3 mb-2  rounded-lg font-medium'}),
        help_text="Your password should contain at least 8 characters."
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'w-full px-6 py-3 mb-2 rounded-lg font-medium'}),
        help_text="Please enter the same password as above, for verification."
    )
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
            'contact_num',
        )

        widgets = {
            'email' : forms.TextInput(attrs={'class': 'w-full py-3 px-6 mb-2 rounded-lg font-medium items-center'}),
            'first_name' : forms.TextInput(attrs={'class': 'w-full px-6 py-3 mb-2 rounded-lg font-medium'}),
            'last_name' : forms.TextInput(attrs={'class': 'w-full px-6 py-3 mb-2 rounded-lg font-medium'}),   
            'age' : forms.NumberInput(attrs={'class': 'w-full px-6 py-3 mb-2 rounded-lg font-medium'}),
            'gender' : forms.Select(attrs={'class': 'w-full px-6 py-3 mb-2 rounded-lg font-medium'}),
            'home_address' : forms.TextInput(attrs={'class': 'w-full px-6 py-3 mb-2 rounded-lg font-medium'}), 
            'date_of_birth' : forms.TextInput(attrs={'class': 'w-full px-6 datepicker py-3 mb-2 rounded-lg font-medium'}), 
            'contact_num' : forms.TextInput(attrs={'class': 'w-full px-6 py-3 mb-2 rounded-lg font-medium'}), 
        }

    


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your email',
        'class': 'w-full px-6 py-3 mb-2 border border-slate-600 rounded-lg font-medium'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full px-6 py-3 mb-2 border border-slate-600 rounded-lg font-medium'
    }))

    
    