from django.db import models

# Create your models here.

ANIMAL_TYPE = [
    ("Dog", "Dog"),
    ("Cat", "Cat"),
    ("Others", "Others")
]

GENDER = [
    ("F", "Female"),
    ("M", "Male")
]

PET_SIZE = [
    ("S", "Small"),
    ("M", "Medium"),
    ("L", "Large"),
]

class PetTbl(models.Model):
    petID = models.BigAutoField(primary_key=True)
    petName = models.CharField(max_length=50, null=False)
    animalType = models.CharField(max_length=10, choices=ANIMAL_TYPE)
    breed = models.CharField(max_length=50, null=False)
    petAge = models.IntegerField(null=False)
    petGender = models.CharField(max_length=10, choices=GENDER)
    petSize = models.CharField(max_length=10, choices=PET_SIZE)
    petDescription = models.TextField()
    dateAcquired = models.DateField(null=False)

class PetMedicalTbl(models.Model):
    medID = models.BigAutoField(primary_key=True)
    