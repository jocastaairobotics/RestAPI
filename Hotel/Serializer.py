from .models import Hotel
from rest_framework import serializers


class HotelSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    address = serializers.CharField()
    manager_name = serializers.CharField(max_length=50)
    manager_phone = serializers.CharField(max_length=13)
    manager_email = serializers.EmailField()


class HotelModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'
