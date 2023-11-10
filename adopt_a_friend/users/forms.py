from django import forms
from django.forms import inlineformset_factory
from .models import Users, Profile, Preference, PersonalityPreference
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UsersForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'mt-2 border-2 border-black w-full px-6 py-3 mb-2 rounded-lg font-medium'}),
        help_text="Your password should contain at least 8 characters."
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'mt-2 border-2 border-black w-full px-6 py-3 mb-2 rounded-lg font-medium'}),
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
            'email' : forms.TextInput(attrs={'class': 'mt-2 border-2 border-black w-full px-6 py-3 mb-2 rounded-lg font-medium'}),
            'first_name' : forms.TextInput(attrs={'class': 'mt-2 border-2 border-black w-full px-6 py-3 mb-2 rounded-lg font-medium'}),
            'last_name' : forms.TextInput(attrs={'class': 'mt-2 border-2 border-black w-full px-6 py-3 mb-2 rounded-lg font-medium'}),   
            'age' : forms.NumberInput(attrs={'class': 'mt-2 border-2 border-black w-full px-6 py-3 mb-2 rounded-lg font-medium'}),
            'gender' : forms.Select(attrs={'class': 'mt-2 border-2 border-black w-full px-6 py-3 mb-2 rounded-lg font-medium'}),
            'home_address' : forms.TextInput(attrs={'class': 'mt-2 border-2 border-black w-full px-6 py-3 mb-2 rounded-lg font-medium'}), 
            'date_of_birth' : forms.TextInput(attrs={'class': 'mt-2 border-2 border-black w-full px-6 py-3 mb-2 rounded-lg font-medium date-picker'}), 
            'contact_num' : forms.TextInput(attrs={'class': 'mt-2 border-2 border-black w-full px-6 py-3 mb-2 rounded-lg font-medium'}), 
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

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = (
            'home_address', 
            'contact_num',
            'user_bio',
        )

        widgets = {
            'home_address' : forms.TextInput(attrs={'class': 'w-full px-6 py-3 mb-2 rounded-lg font-medium'}), 
            'contact_num' : forms.TextInput(attrs={'class': 'w-full px-6 py-3 mb-2 rounded-lg font-medium'}), 
            'user_bio' : forms.Textarea(attrs={'class': 'w-full px-6 py-3 mb-2 rounded-lg font-medium'}), 
        }

        labels = {
            'home_address': 'Home Address:',  
            'contact_num': 'Contact Number:',
            'user_bio': 'User Bio:',
        }
    
class ProfilePictureUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'image',
        )

class PreferenceForm(forms.ModelForm):
    class Meta:
        model = Preference
        exclude = ['preferenceId', 'adopter']

        widgets = {
            'preferredAnimalType' : forms.Select(attrs={'class': 'mt-2 border-2 border-black w-full px-6 py-3 mb-2 rounded-lg font-medium'}), 
            'preferredBreed' : forms.TextInput(attrs={'class': 'mt-2 border-2 border-black w-full px-6 py-3 mb-2 rounded-lg font-medium'}), 
            'preferredAge' : forms.NumberInput(attrs={'class': 'mt-2 border-2 border-black w-full px-6 py-3 mb-2 rounded-lg font-medium'}),
            'preferredGender' : forms.Select(attrs={'class': 'mt-2 border-2 border-black w-full px-6 py-3 mb-2 rounded-lg font-medium'}), 
            'preferredSize' : forms.Select(attrs={'class': 'mt-2 border-2 border-black w-full px-6 py-3 mb-2 rounded-lg font-medium'}),             
            'preferredColor': forms.Select(attrs={'class': 'mt-2 border-2 border-black w-full px-6 py-3 mb-2 rounded-lg font-medium'}), 
            'preferredSpayedorNeutered' : forms.CheckboxInput(attrs={'class' : 'ml-4'}),
            'preferredHealthCondition' : forms.Select(attrs={'class': 'mt-2 border-2 border-black w-full px-6 py-3 mb-2 rounded-lg font-medium'}), 
        }

        labels = {
            'preferredAnimalType': 'Preferred Animal Type:',
            'preferredBreed': 'Preferred Breed:',
            'preferredAge': 'Preferred Age of the Pet:',
            'preferredGender': 'Preferred Gender of the Pet:',
            'preferredSize': 'Preferred Size of the Pet:',
            'preferredColor': 'Preferred Color of the Pet:',
            'preferredSpayedorNeutered': 'Preference for a Spayed or Neutered Pet:',
            'preferredHealthCondition': 'Preferred Health Condition of the Pet:',
        }

class PersonalityPreferenceForm(forms.ModelForm):
    class Meta:
        model = Preference
        exclude = ['preferenceId']

        widgets = {
            'preferredPersonality': forms.Select(attrs={'class': 'mt-2 border-2 border-black w-full px-6 py-3 mb-2 rounded-lg font-medium'}), 
        }

PersonalityPreferenceFormSet = inlineformset_factory(Preference, PersonalityPreference, form=PersonalityPreferenceForm, extra=3, can_delete=False)
