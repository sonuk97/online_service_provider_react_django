from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .serializers import userSerializer,loginserializer
from rest_framework.authtoken.models import Token
import random
from django.core.mail import send_mail
from django.conf import settings
from backend.models import CustomUser
from django.contrib import messages
from rest_framework import status
from django.contrib.auth import authenticate,login,logout


def index(request):
    return Response('ok')

@api_view(['POST'])
def register(request):
    serializer = userSerializer(data=request.data)
    
    if serializer.is_valid():
        username = serializer.validated_data.get('username')
        email = serializer.validated_data.get('email')
        passw = str(random.randint(100000, 999999))
        sub = 'Login Details'
        message = "Your Login details are:\nUsername: {}\nPassword: {}".format(username, passw)
        send_mail(sub, message, settings.EMAIL_HOST_USER, [email])
        messages.info(request, 'Please check your mail for login details')

        # Create user with the randomly generated password
        user = CustomUser.objects.create_user(
            username=request.data.get('username'),
            password=passw,
            first_name=request.data.get('fname'),
            last_name=request.data.get('lname'),
            email=request.data.get('email'),
            usertype=request.data.get('usertype'),
            phone_number=request.data.get('phoneNumber'),
            address=request.data.get('address'),
            status=request.data.get('status'),
            image=request.data.get('image'),
            department=request.data.get('department'),
            service=request.data.get('services'),
        )
        user.save()
        token = Token.objects.create(user = user)
        print(token.key)
        print(serializer.data)
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    
    
    
@api_view(['POST'])    
def login(request):
    serializer = loginserializer(data=request.data)
    if serializer.is_valid():
        user = authenticate(username = request.data.get('username'),password = request.data.get('password'))
        print(user)
        if user:
            token = Token.objects.get(user = user)
            print(token.key)
            use = CustomUser.objects.get(username = user)
            e=userSerializer(use,many=True)
            return Response({'token':token.key,'usertype': user.usertype})
       
        else:
            return Response(serializer.errors)