from django.urls import path, include
from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'uuid', 'car_category', 'brand_id', 'year', 'brand', 'mark_id', 'model', 'eng_power']
