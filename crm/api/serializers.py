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