from django.urls import path , include
from . import views
from rest_framework import routers


rr = routers.DefaultRouter()
rr.register('', views.orderitem)

rrr = routers.DefaultRouter()
rrr.register('', views.order)

urlpatterns = [
    
    path('',views.Home_listAPI,name='Home_list'),
    # path('orderitems/',views.jsonOrderItem,name='Shopping_Cart'),
    path('itemorder/', include(rr.urls)),
    path('order/', include(rrr.urls)),
    # path('order/',views.orderitem,name='Shopping_Cart'),

    path('Recommended/',views.Recommended_listAPI,name='Recommended'),
    

]