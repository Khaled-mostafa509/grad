from django.db import models
from home.models import Products

# Create your models here.

class Recommended(models.Model):
    product_name = models.ForeignKey("Products", on_delete=models.CASCADE) 
    recomended_devices = models.CharField( max_length=1000) 
    
    def __str__(self):
        return self.recommended_devices