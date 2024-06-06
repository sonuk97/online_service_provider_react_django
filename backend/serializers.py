from rest_framework import serializers
from .models import CustomUser



class userSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields =  fields = ['username', 'email', 'first_name', 'last_name',  'usertype','location','address','status','phone_number','image','agency_name','department','service' ]  # Exclude 'password'
        
        
class loginserializer(serializers.Serializer):
     username = serializers.CharField()
     password = serializers.CharField()