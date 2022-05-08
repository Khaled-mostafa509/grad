from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    user_type_choices=((1,"Admin"),(2,"Customer"),(3,"Company"))
    user_type=models.CharField( max_length=255,choices=user_type_choices,default=2)
#   is_person = models.BooleanField(default=False)
#   is_company = models.BooleanField(default=False)
class AdminUser(models.Model):
    # person = models.OneToOneField(
    #   settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    auth_user_id = models.OneToOneField("User", on_delete=models.CASCADE)
    first_name = models.CharField( max_length=15)
    last_name = models.CharField( max_length=15)

class Person(models.Model):
    # person = models.OneToOneField(
    #   settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    auth_user_id = models.OneToOneField("User", on_delete=models.CASCADE)
    user=User
    first_name = models.CharField( max_length=15)
    last_name = models.CharField( max_length=15)
    phone_number = models.CharField( max_length=14)
    image = models.ImageField( upload_to='profile/')

class Company(models.Model):
    # company = models.OneToOneField(
    #     settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    auth_user_id = models.OneToOneField("User", on_delete=models.CASCADE)
    company_name = models.CharField( max_length=15)
    phone_number = models.CharField( max_length=14)
    logo = models.ImageField( upload_to='profile/')
