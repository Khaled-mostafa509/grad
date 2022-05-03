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

        
# class Order_ItemSerializers(serializers.ModelSerializer):
#     user_name = serializers.CharField(source='user.username')
#     item_name = serializers.CharField(source='item.Name')
#     class Meta:
#         model = OrderItem
#         fields = ['id','ordered','quantity','user_name','item_name']
class  jsonOrderItem(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"
        
class  jsonOrder(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"      
        
