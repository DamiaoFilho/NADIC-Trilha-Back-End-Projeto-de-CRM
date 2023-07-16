from django.contrib.auth.models import User

from rest_framework import serializers
from crm.models import *


class stockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class companySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user