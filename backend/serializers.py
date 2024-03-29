from rest_framework import serializers
from django.contrib.auth.models import User
from .models import classcreate,Addwork,Submitedworks
import datetime
import pytz
from rest_framework.settings import api_settings
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

class classcreateSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source='user.username', read_only=True)
   
    class Meta:

        model=classcreate
        fields = ['username','classname','created','user','id','discription']


class AddworkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Addwork
        fields = '__all__'


class SubmitedWorksSerializer(serializers.ModelSerializer):
    student = serializers.CharField(source='student.username', read_only=True)
    created = serializers.DateTimeField(format="%d-%m-%Y %H-%M-%p", input_formats=['%d-%m-%Y', 'iso-8601'], default_timezone=None)
    
    
    class Meta:
        model=Submitedworks
        fields=['student','Message','file','status','created']


        
    


class EditClassSerializer(serializers.ModelSerializer):
    class Meta:
        model=classcreate
        fields=['classname','discription']



    














