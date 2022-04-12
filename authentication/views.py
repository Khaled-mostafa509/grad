from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from authentication.serializers import RegisterSerializers ,LoginSerializers
from rest_framework import response,status
from django.contrib.auth import authenticate


# Create your views here.
class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializers
    
    def post(self,request):
        serializer =self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data,status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializers
    def post(self,request):
        email=request.data.get('email',None)
        password=request.data.get('password',None)
        user =authenticate(username=email,password=password)
        if user:
            serializer = self.serializer_class(user)
            return response.Response(serializer.data,status=status.HTTP_200_OK)
        return response.Response({'message':"Invalid credentialsn try again"},status=status.HTTP_401_UNAUTHORIZED)
    
# class UserList(GenericAPIView):
    # permission_classes = (IsAuthenticatedOrWriteOnly,)
#     serializer_class = UserSerializer

#     def post(self, request, format=None):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)