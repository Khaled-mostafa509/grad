from .models import Products ,OrderItem , Order ,Recommended
from .serializers import HomeSerializers  ,RecommendedSerializers ,jsonOrder,jsonOrderItem
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, permissions
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from authentications.models import User

@api_view(['GET','Post'])
def Home_listAPI(request):
    all_ads=Products.objects.all()
    permission_classes = [permissions.IsAdminUser]
    return Response(HomeSerializers(all_ads,many=True).data)

@api_view(['GET','Post'])
def Recommended_listAPI(request):
    all_ads=Recommended.objects.all()
    # permission_classes = [permissions.IsAdminUser]
    return Response(RecommendedSerializers(all_ads,many=True).data)

# @api_view(['POST','GET'])
# @login_required
# def add_to_cart(request):
#     item = get_object_or_404(Products )
#     order_item, created = OrderItem.objects.get_or_create(
#         item=item,
#         user=request.user,
#         ordered=False
#     )
#     order_qs = Order.objects.filter(user=request.user, ordered=False)
#     if order_qs.exists():
#         order = order_qs[0]

#         if order.items.filter().exists():
#             order_item.quantity += 1
#             order_item.save()
#             all_orders= OrderItem.objects.all()
#             # messages.info(request, "This item quantity was updated.")
#             return Response(Order_ItemSerializers(all_orders,many=True).data)
#         else:
#             order.items.add(order_item)
#             all_orders= OrderItem.objects.all()
#             # messages.info(request, "This item was added to your cart.")
#             return Response(Order_ItemSerializers(all_orders,many=True).data)
#     else:
#         order = Order.objects.create(user=request.user)
#         order.items.add(order_item)
#         all_orders= OrderItem.objects.all()
#         # messages.info(request, "This item was added to your cart.")
#         return Response(Order_ItemSerializers(all_orders,many=True).data)
class orderitem(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = jsonOrderItem


class order(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = jsonOrder
    
    
# class order(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = jsonOrder