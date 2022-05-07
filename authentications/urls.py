from django.urls import path
from .views import PersonRegistrationView,CompanyRegistrationView
# from .views import LoginAPI

app_name = 'authentications'

urlpatterns = [
    
    path('registration/user/', PersonRegistrationView.as_view(), name='register-user'),
    path('registration/company/', CompanyRegistrationView.as_view(), name='register-company'),
    # path('login/',LoginAPI.as_view(),name='login user')
]