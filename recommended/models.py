from django.db import models
from .contentbased import tst

# Create your models here.

class Recommended(models.Model):
    recommended_name=models.CharField((tst), max_length=200)
    
    def __str__(self):
        return self.recommended_name