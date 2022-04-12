from django.urls import path , include
from . import views

urlpatterns = [
    
    path('',views.Recommended_listAPI, name='recommended name'),
    

]