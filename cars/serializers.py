from rest_framework import serializers
from .models import Car, Owner

class OwnerSerializer(serializers.ModelSerializer):
   # This is the owner serializer
    class Meta:
        model = Owner
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
   # This is the car serializer
    car_owner = OwnerSerializer()
    class Meta:
        model = Car
        fields = '__all__'

