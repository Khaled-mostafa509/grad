from django.db import models

# Create your models here.
from django.db import models


class Products(models.Model):
    
    Name=models.CharField( max_length=50)
    description = models.TextField(max_length=1000)
    Category=models.ForeignKey("Category", on_delete=models.CASCADE)
    price = models.CharField(max_length=10,null= True)
    Production_country = models.CharField( max_length=50)
    image = models.ImageField( upload_to='media_files/',null= True)
    
    
    
    
    def __str__(self):
        return self.Name
class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    
