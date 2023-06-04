from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model
 
User = get_user_model()

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.product
        fields = '__all__'

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'