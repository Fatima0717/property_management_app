# urls.py
from django.contrib import admin
from django.urls import path
from properties import views  # Import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('properties/', views.property_list, name='property_list'),
    # Add other URL patterns as needed
]
