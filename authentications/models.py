from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

class User(AbstractUser):
    
  is_person = models.BooleanField(default=False)
  is_company = models.BooleanField(default=False)
  
@receiver(post_save, sender=settings.AUTH_USER_MODEL)    
def create_auth_token(sender, instance=None,created=False,**kwargs):
  if created:
    Token.objects.create(user=instance)
  


class Person(models.Model):
    # person = models.OneToOneField(
    #   settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    user=models.OneToOneField("User",related_name="Person",  on_delete=models.CASCADE)
    first_name = models.CharField( max_length=15)
    last_name = models.CharField( max_length=15)
    phone_number = models.CharField( max_length=14)
    image = models.ImageField( upload_to='profile/')

    def __str__(self):
        return self.person.username

class Company(models.Model):
    # company = models.OneToOneField(
    #     settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user=models.OneToOneField("User",related_name="Company",  on_delete=models.CASCADE)
    company_name = models.CharField( max_length=15)
    phone_number = models.CharField( max_length=14)
    logo = models.ImageField( upload_to='profile/')

    def __str__(self):
        return self.company_name.username