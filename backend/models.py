from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    usertype= models.CharField(default=1,max_length=10)
    agency_name=models.CharField(max_length=255, null=True)
    phone_number=models.CharField(max_length=255, null=True)
    address=models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=20, null=True)
    service = models.CharField(max_length=20, null=True)
    location = models.CharField(max_length=20, null=True)
    image = models.ImageField(blank=True,upload_to="images/",null=True) 
    department = models.CharField(max_length=20, null=True)
    
    

    
    
