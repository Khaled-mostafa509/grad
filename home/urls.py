from django.urls import path , include
from . import views
from rest_framework import routers


rr = routers.DefaultRouter()
rr.register('', views.orderitem)

rrr = routers.DefaultRouter()
rrr.register('', views.order)


r = routers.DefaultRouter()
r.register('', views.product)
urlpatterns = [
    
    path('Recommended/',views.Recommended_listAPI,name='Recommended'),
    path('', include(r.urls)),
    path('itemorder/', include(rr.urls)),
    path('order/', include(rrr.urls)),
    

]