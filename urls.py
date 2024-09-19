from django.contrib import admin
from django.urls import path
from . import views  # Import your view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),  # Add this line for the home page
]
