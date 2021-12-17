from django.urls import path, include
from rest_framework import routers
from cars.views import *


urlpatterns = [
    path('cars/', CarAPIView.as_view()),
    
]
