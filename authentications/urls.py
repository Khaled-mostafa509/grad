from django.urls import path,include
from authentications.views import SellerRegistrationView,BuyerRegistrationView
# from rest_framework import routers

# r = routers.DefaultRouter()
# r.register('', views.CompanyRegistrationView)

# rr = routers.DefaultRouter()
# rr.register('', views.PersonRegistrationView)
urlpatterns = [
    # path('registration/user/', include(rr.urls)),

    # path('registration/user/', PersonRegistrationView.as_view(), name='register-user'),
    # path('registration/company/', CompanyRegistrationView.as_view(), name='register-company'),
    # path('registration/company/', include(r.urls)),
    # path('login/',LoginAPI.as_view(),name='login user')
    path('registration/seller/', SellerRegistrationView.as_view(), name='register-seller'),
    path('registration/buyer/', BuyerRegistrationView.as_view(), name='register-buyer'),
]