from django.db import models
from authentications.models import User

# Create your models here.





class Products(models.Model):
    
    Name=models.CharField( max_length=50)
    description = models.TextField(max_length=1000)
    Category=models.CharField(max_length=25)
    price = models.CharField(max_length=10,null= True)
    Production_country = models.CharField( max_length=50)
    image = models.ImageField( upload_to='product_image/',null= True)

    
    
    
    
    def __str__(self):
        return self.Name
    
class Recommended(models.Model):
    product_name = models.ForeignKey("Products", on_delete=models.CASCADE) 
    recomended_devices = models.ManyToManyField("Products",related_name="aa") 
    
    def __str__(self):
        return self.recomended_devices
       

class OrderItem(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    item = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.Name}"

    def get_total_item_price(self):
        return self.quantity * self.item.price
    
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
