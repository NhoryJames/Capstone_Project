from django import forms
from pets.models import *

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = (
            'petName',
            'animalType',
            'breed',
            'petAge',
            'petGender',
            'petSize',
            'petPersonality',
            'petColor',
            'petDescription',
            'isTrained',
        )

        widgets = {
            'petName' : forms.TextInput(attrs={'class': 'mt-2 border-2 border-black w-full px-6 py-3 mb-2 rounded-lg font-medium'}), 
            'animalType' : forms.Select(attrs={'class': 'mt-2 border-2 border-black w-full px-6 py-3 mb-2 rounded-lg font-medium'}), 
            'breed' : forms.TextInput(attrs={'class': 'mt-2 border-2 border-black w-full px-6 py-3 mb-2 rounded-lg font-medium'}), 
            'petAge' : forms.NumberInput(attrs={'class': 'mt-2 border-2 border-black w-full px-6 py-3 mb-2 rounded-lg font-medium'}),
            'petGender' : forms.Select(attrs={'class': 'mt-2 border-2 border-black w-full px-6 py-3 mb-2 rounded-lg font-medium'}), 
            'petSize' : forms.Select(attrs={'class': 'mt-2 border-2 border-black w-full px-6 py-3 mb-2 rounded-lg font-medium'}), 
            'petPersonality': forms.Select(attrs={'class': 'mt-2 border-2 border-black w-full px-6 py-3 mb-2 rounded-lg font-medium'}), 
            'petColor': forms.Select(attrs={'class': 'mt-2 border-2 border-black w-full px-6 py-3 mb-2 rounded-lg font-medium'}), 
            'petDescription' : forms.Textarea(attrs={'class': 'mt-2 border-2 border-black w-full px-6 py-3 mb-2 rounded-lg font-medium'}), 
            'isTrained' : forms.CheckboxInput(attrs={'class' : 'ml-4'})
        }

        labels = {
            'petName' : 'Pet Name:',
            'animalType' : 'Animal Type:',
            'breed' : 'Breed:',
            'petAge' : 'Pet Age:',
            'petGender' : 'Pet Gender:',
            'petSize' : 'Pet Size:',
            'petPersonality': 'Pet Personality:',
            'petColor': 'Pet Color:',
            'petDescription' : 'Pet Description:',
            'isTrained' : 'Is the pet trained? (check the box if yes):'
        }

class PetMedicalForm(forms.ModelForm):
    class Meta:
        model = PetMedical
        fields = (
            'petWeight',
            'isVaccinated',
            'isNeutered_or_Spayed',
            'healthCondition',
            'disease',
            'comment',
        )
    
        widgets = {
            'petWeight' : forms.TextInput(attrs={'class': 'mt-2 border-2 border-black w-full px-6 py-3 mb-2 rounded-lg font-medium'}), 
            'isVaccinated' : forms.CheckboxInput(attrs={'class' : 'ml-4'}),
            'isNeutered_or_Spayed' : forms.CheckboxInput(attrs={'class' : 'ml-4'}),
            'healthCondition' : forms.Select(attrs={'class': 'mt-2 border-2 border-black w-full px-6 py-3 mb-2 rounded-lg font-medium'}), 
            'disease' : forms.TextInput(attrs={'class': 'mt-2 border-2 border-black w-full px-6 py-3 mb-2 rounded-lg font-medium'}), 
            'comment' : forms.Textarea(attrs={'class': 'mt-2 border-2 border-black w-full px-6 py-3 mb-2 rounded-lg font-medium'}), 
        }

        labels = {
            'petWeight' : 'Weight (KG):',
            'isVaccinated' : 'Is the pet vaccinated? (check the box if yes):',
            'isNeutered_or_Spayed' :  'Is the pet spayed/neutered? (check the box if yes):',
            'healthCondition' :  'What is the current health condition of the pet?',
            'disease' : 'Disease (if any):',
            'comment' : 'Vet Comment:'
        }

