from django.db import models
from users.models import Users
from django.db.models import F
from django.utils.text import slugify
from django.urls import reverse
from django.utils import timezone

COLOR_CHOICES = (
    ('Black', 'Black'),
    ('White', 'White'),
    ('Gray', 'Gray'),
    ('Brown', 'Brown'),
    ('Orange', 'Orange'),
    ('Cream', 'Cream'),
    ('Bi-color', 'Bi-color'),
    ('Tricolor', 'Tricolor')
)

PERSONALITY_CHOICES = (
    ('Playful', 'Playful'),
    ('Cuddly', 'Cuddly'),
    ('Energetic', 'Energetic'),
    ('Laid_back', 'Laid-back'),
    ('Curious', 'Curious'),
    ('Social', 'Social'),
    ('Independent', 'Independent'),
    ('Shy/Timid', 'Shy/Timid'),
    ('Bold/Confident', 'Bold/Confident'),
    ('Intelligent', 'Intelligent'),
    ('Mischievous', 'Mischievous'),
    ('Reserved', 'Reserved'),
    ('Protective', 'Protective'),
    ('Adventurous', 'Adventurous'),
    ('Affectionate', 'Affectionate'),
    ('Patient', 'Patient'),
    ('Stubborn', 'Stubborn'),
    ('Gentle', 'Gentle'),
    ('Sociable', 'Sociable'),
    ('Talkative', 'Talkative'),
)

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
)

ANIMAL_TYPES_CHOICES = (
    ('Dog', 'Dog'),
    ('Cat', 'Cat')
)

PET_SIZE_CHOICES = (
    ('Extra Small', 'Extra Small'),
    ('Small', 'Small'),
    ('Medium', 'Medium'),
    ('Large', 'Large')
)

HEALTH_CONDITIONS = (
    ('Healthy', 'Healthy'),
    ('With Disease/Illness', 'With Disease/Illness'),
    ('Chronic Condition', 'Chronic Condition'),
    ('Under Treatment', 'Under Treatment'),
    ('Recovering', 'Recovering'),
    ('Injured', 'Injured'),
    ('Behavioral Issues', 'Behavioral Issues'),
    ('Senior Care', 'Senior Care'),
)

def generate_pet_key():
    last_record = Pet.objects.order_by('-petId').first()
    if last_record is not None:
        last_id = int(last_record.petId[3:])  # Extract the numeric part of the petId
        new_id = last_id + 1
    else:
        new_id = 1
    return f'PET{str(new_id).zfill(4)}'

def generate_med_key():
    last_record = Pet.objects.order_by('-medId').first()
    if last_record is not None:
        new_id = F('medId') + 1
    else:
        new_id = 1
    return f'MED{str(new_id).zfill(4)}'

class Pet(models.Model):
    petId = models.CharField(max_length=10, default=generate_pet_key, primary_key=True, unique=True)
    petName = models.CharField(max_length=50, null=False, blank=False, unique=True)
    animalType = models.CharField(max_length=20, choices=ANIMAL_TYPES_CHOICES, null=False, blank=False)
    breed = models.CharField(max_length=50, null=False, blank=False)
    petAge = models.IntegerField(null=False, blank=False)
    petGender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=False, blank=False, default="Others")
    petSize = models.CharField(max_length=20, choices=PET_SIZE_CHOICES, null=False, blank=False)
    petColor = models.CharField(max_length=20, choices=COLOR_CHOICES, null=False, blank=False, default="Brown")
    petDescription = models.TextField(max_length=500, blank=True, null=True)
    petPersonality = models.CharField(max_length=50, choices=PERSONALITY_CHOICES, blank=False, null=False, default="Intelligent")
    dateAcquired = models.DateField(blank=False, null=False, default=timezone.now)
    isTrained = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.petName
    
    def get_absolute_pet_url(self):
        return reverse("pet_profile", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.petName}")
        super(Pet, self).save(*args, **kwargs)

class PetImage(models.Model):
    petId = models.ForeignKey(Pet, null=False, blank=False, on_delete=models.CASCADE)
    petImage = models.ImageField()

class PetMedical(models.Model):
    petId = models.ForeignKey(Pet, null=False, blank=False, on_delete=models.CASCADE)
    petWeight = models.CharField(max_length=30, null=False, default='0')
    isVaccinated = models.BooleanField()
    isNeutered_or_Spayed = models.BooleanField()
    healthCondition = models.CharField(max_length=30, null=False, choices=HEALTH_CONDITIONS)
    disease = models.CharField(max_length=100, null=False)
    comment = models.TextField(max_length=500, blank=True, null=True)
    