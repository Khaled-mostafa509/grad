from rest_framework import serializers
from .models import Products , Order , OrderItem ,Recommended

class HomeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
        
class RecommendedSerializers(serializers.ModelSerializer):
    product= serializers.CharField(source='product_name.Name')
    class Meta:
        model = Recommended
        fields = ['id','product','recomended_devices']

        
class  jsonOrderItem(serializers.ModelSerializer):
    item= serializers.CharField(source='item.Name')
    class Meta:
        model = OrderItem
        fields = "__all__"
        
class  jsonOrder(serializers.ModelSerializer):
    # items= serializers.CharField(source=f"{OrderItem.quantity} of {OrderItem.item}")
    class Meta:
        model = Order
        fields = "__all__"      
        
