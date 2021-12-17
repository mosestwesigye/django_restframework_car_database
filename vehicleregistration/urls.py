from django.contrib import admin
from django.urls import path, include

"""
CarApi and admin url paths
"""
urlpatterns = [
    path('api/v1/', include ('cars.urls')),
    path('admin/', admin.site.urls),
    
]
