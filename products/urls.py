from django.urls import path , include
from . import api

urlpatterns = [
    
    path('category',api.Category_list, name='category_list'),
    path('',api.Products_listAPI,name='Products_list'),

]