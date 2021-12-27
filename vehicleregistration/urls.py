from django.contrib import admin
from django.urls import path, include

"""
CarApi and admin url paths
"""
urlpatterns = [
    path('', include ('cars.urls')),
    path('admin/', admin.site.urls),
    
]
