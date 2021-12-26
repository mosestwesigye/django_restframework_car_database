from django.urls import path, include
from rest_framework import routers
from cars.views import *

"""
Car URLPath
"""
urlpatterns = [
    path('', CarAPIView.as_view()),
    
]
