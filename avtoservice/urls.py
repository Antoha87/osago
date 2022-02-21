from django.urls import path, include
from rest_framework import routers
from .views import CarModelViewSet

Router = routers.DefaultRouter()
Router.register('car', CarModelViewSet)

urlpatterns = [
    path('api/', include(Router.urls)),
    ]
