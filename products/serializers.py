from rest_framework import serializers
from .models import Products , Category

class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
        
class CategorySerializers(serializers.ModelSerializer):
    class Meta :
        model = Category
        fields = '__all__'