from .models import Products ,OrderItem , Order ,Recommended
from .serializers import HomeSerializers  ,RecommendedSerializers ,jsonOrder,jsonOrderItem
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, permissions
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required




@api_view(['GET','Post'])
def Recommended_listAPI(request):
    all_ads=Recommended.objects.all()
    # permission_classes = [permissions.IsAdminUser]
    return Response(RecommendedSerializers(all_ads,many=True).data)

class product(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = HomeSerializers

class orderitem(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = jsonOrderItem


class order(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = jsonOrder
    
    
