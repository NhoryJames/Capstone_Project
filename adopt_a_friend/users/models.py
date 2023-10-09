from django.db import models
from django.utils import timezone
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class CustomAccountManager(BaseUserManager):
    # ------ FOR CREATING USER ACCOUNTS ------ #
    def create_user(self, email, password, first_name, last_name, age, date_of_birth, home_address, contact_num, user_bio, **other_fields):
        email = self.normalize_email(email)

        if not email:
            raise ValueError("Email address is required")
        if not password:
            raise ValueError("Password is required")
        if not first_name:
            raise ValueError("First name is required")
        if not last_name:
            raise ValueError("Last name is required")
        if age is None:
            raise ValueError("Age is required")
        if date_of_birth is None:
            raise ValueError("Date of birth is required")
        if not home_address:
            raise ValueError("Home address is required")
        if not contact_num:
            raise ValueError("Contact number is required")
        
        if age < 0:
            raise ValueError("Age cannot be negative")
        if not contact_num.isdigit():
            raise ValueError("Contact number should contain only digits")

        user = self.model(email=email, first_name=first_name, last_name=last_name, age=age, date_of_birth=date_of_birth, home_address=home_address, contact_num=contact_num, user_bio=user_bio)
        user.set_password(password)
        user.save()
        return user
    
    # ------ FOR CREATING SUPERUSER/ADMIN ACCOUNTS ------ #

    def create_superuser(self, email, password, first_name, last_name, age, date_of_birth, home_address, contact_num, user_bio="", **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Staff must be assigned to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')

        # Remove the "self" argument here
        return self.create_user(email, password, first_name, last_name, age, date_of_birth, home_address, contact_num, user_bio, **other_fields)


class UserTbl(AbstractBaseUser, PermissionsMixin):
     
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    home_address = models.CharField(max_length=200)
    contact_num = models.CharField(max_length=15)
    user_bio = models.TextField(max_length=500, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'age', 'date_of_birth', 'home_address', 'contact_num', 'user_bio']

    def __str__(self):
        return self.email
