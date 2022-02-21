from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import CarSerializer
from .models import Car


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]
