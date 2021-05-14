from rest_framework import serializers
from django.contrib.auth.models import User
from .models import classcreate,Addwork,Submitedworks

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
    class Meta:
        model=Submitedworks
        fields=['student','created','Message','file']

















