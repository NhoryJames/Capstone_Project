from django import forms
from pets.models import Pet

class AddPetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = (
            'petName',
            'animalType',
            'breed',
            'petAge',
            'petGender',
            'petSize',
            'petDescription',
            'isTrained',
        )

        widgets = {
            'petName' : forms.TextInput(attrs={'class': 'w-full px-6 py-3 mb-2 rounded-lg font-medium'}), 
            'animalType' : forms.Select(attrs={'class': 'w-full px-6 py-3 mb-2 rounded-lg font-medium'}), 
            'breed' : forms.TextInput(attrs={'class': 'w-full px-6 py-3 mb-2 rounded-lg font-medium'}), 
            'petAge' : forms.NumberInput(attrs={'class': 'w-full px-6 py-3 mb-2 rounded-lg font-medium'}),
            'petGender' : forms.Select(attrs={'class': 'w-full px-6 py-3 mb-2 rounded-lg font-medium'}), 
            'petSize' : forms.Select(attrs={'class': 'w-full px-6 py-3 mb-2 rounded-lg font-medium'}), 
            'petDescription' : forms.Textarea(attrs={'class': 'w-full px-6 py-3 mb-2 rounded-lg font-medium'}), 
        }

        labels = {
            'petName' : 'Pet Name:',
            'animalType' : 'Animal Type:',
            'breed' : 'Breed:',
            'petAge' : 'Pet Age:',
            'petGender' : 'Pet Gender:',
            'petSize' : 'Pet Size:',
            'petDescription' : 'Pet Description:',
            'isTrained' : 'Is the pet trained?'
        }