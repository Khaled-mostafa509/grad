from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    
  is_person = models.BooleanField(default=False)
  is_company = models.BooleanField(default=False)

class Person(models.Model):
    person = models.OneToOneField(
      settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField( max_length=15)
    last_name = models.CharField( max_length=15)
    phone_number = models.CharField( max_length=14)
    image = models.ImageField( upload_to='profile/')

    def __str__(self):
        return self.person.username

class Company(models.Model):
    company = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_name = models.CharField( max_length=15)
    phone_number = models.CharField( max_length=14)
    logo = models.ImageField( upload_to='profile/')

    def __str__(self):
        return self.company_name.username