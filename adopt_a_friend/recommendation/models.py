from django.db import models
from users.models import UserTbl

# Create your models here.

def generate_preference_key():
    last_record = PreferenceTbl.objects.order_by('-preferenceId').first()
    if last_record is not None:
        last_id = last_record.id
        new_id = last_id + 1
    else:
        new_id = 1
    return f'PR{str(new_id).zfill(3)}'

def generate_breed_preference_key():
    last_record = BreedPreferenceTbl.objects.order_by('-breedpfId').first()
    if last_record is not None:
        last_id = last_record.id
        new_id = last_id + 1
    else:
        new_id = 1
    return f'BPR{str(new_id).zfill(3)}'

def generate_color_preference_key():
    last_record = PreferenceTbl.objects.order_by('-colorpfId').first()
    if last_record is not None:
        last_id = last_record.id
        new_id = last_id + 1
    else:
        new_id = 1
    return f'CPR{str(new_id).zfill(3)}'

def generate_personality_preference_key():
    last_record = PreferenceTbl.objects.order_by('-personalitypfId').first()
    if last_record is not None:
        last_id = last_record.id
        new_id = last_id + 1
    else:
        new_id = 1
    return f'PPR{str(new_id).zfill(3)}'

class PreferenceTbl(models.Model):
    preferenceId = models.CharField(max_length=6, default=generate_preference_key, primary_key=True, unique=True)
    Id = models.OneToOneField(UserTbl, on_delete=models.CASCADE)
    preferredAnimalType = models.CharField(max_length=20)
    preferredAge = models.IntegerField()
    preferredGender = models.CharField(max_length=20)
    preferredSpayed = models.BooleanField()
    preferredNeutered = models.BooleanField()
    preferredHealthCondition = models.CharField(max_length=50)

class BreedPreferenceTbl(models.Model):
    breedpfId = models.CharField(max_length=6, default=generate_breed_preference_key, primary_key=True, unique=True)
    preferenceId = models.OneToOneField(PreferenceTbl, on_delete=models.CASCADE)
    breed = models.CharField(max_length=50)

class ColorPreferenceTbl(models.Model):
    colorpfId = models.CharField(max_length=6, default=generate_color_preference_key, primary_key=True, unique=True)
    preferenceId = models.OneToOneField(PreferenceTbl, on_delete=models.CASCADE)
    color = models.CharField(max_length=20)

class PersonalityPreferenceTbl(models.Model):
    personalitypfId = models.CharField(max_length=6, default=generate_personality_preference_key, primary_key=True, unique=True)
    preferenceId = models.OneToOneField(PreferenceTbl, on_delete=models.CASCADE)
    personality = models.CharField(max_length=50)

