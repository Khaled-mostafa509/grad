from django.urls import path
from authentications.views import PersonRegistrationView,CompanyRegistrationView,LoginAPI
# from rest_framework import routers

# r = routers.DefaultRouter()
# r.register('', views.CompanyRegistrationView)

# rr = routers.DefaultRouter()
# rr.register('', views.PersonRegistrationView)
urlpatterns = [
    path('registration/user/', PersonRegistrationView.as_view(), name='register-user'),
    path('registration/company/', CompanyRegistrationView.as_view(), name='register-company'),
    path('login/',LoginAPI.as_view(),name='login user')
]