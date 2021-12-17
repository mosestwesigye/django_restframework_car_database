from rest_framework import serializers
from .models import Car, Owner

"""
This is the Owner Serializer Class that will be used in retrieving of information from the DB
"""
class OwnerSerializer(serializers.ModelSerializer):
   # This is the owner serializer
    class Meta:
        model = Owner
        fields = '__all__'

"""
This is the Car Serializer Class that will be used in retrieving of information from the DB
"""
class CarSerializer(serializers.ModelSerializer):
    car_owner = OwnerSerializer()
    class Meta:
        model = Car
        fields = '__all__'

