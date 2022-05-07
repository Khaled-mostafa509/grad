from django.shortcuts import render
from .serializers import PersonCustomRegistrationSerializer, CompanyCustomRegistrationSerializer ,LoginSerializers
from rest_framework.generics import GenericAPIView
from django.contrib.auth import login
from .models import Company,Person
from rest_framework import permissions,viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer

# class PersonRegistrationView(RegisterView):
#     serializer_class = PersonCustomRegistrationSerializer

    
    # def post(self,request):
    #     serializer =self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return response.Response(serializer.data,status=status.HTTP_201_CREATED)
    #     return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   


class LoginAPI(GenericAPIView):
    serializer_class = LoginSerializers
    def post(self,request):
        email=request.data.get('email',None)
        password=request.data.get('password',None)
        user =authenticate(username=email,password=password)
        if user:
            serializer = self.serializer_class(user)
            return response.Response(serializer.data,status=status.HTTP_200_OK)
        return response.Response({'message':"Invalid credentialsn try again"},status=status.HTTP_401_UNAUTHORIZED)

# class CompanyRegistrationView(RegisterView):
#     serializer_class = CompanyCustomRegistrationSerializer
# class CompanyRegistrationView(GenericAPIView):
#     serializer_class = CompanyCustomRegistrationSerializer
class CompanyRegistrationView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanyCustomRegistrationSerializer  
    
class PersonRegistrationView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonCustomRegistrationSerializer 
    # def post(self,request):
    #     serializer =self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return response.Response(serializer.data,status=status.HTTP_201_CREATED)
    #     return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)