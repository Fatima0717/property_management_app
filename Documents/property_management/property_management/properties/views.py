# properties/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Property

@login_required
def profile_view(request):
    profile = request.user.userprofile
    favorite_properties = profile.favorite_properties.all()
    
    return render(request, 'properties/profile.html', {
        'profile': profile,
        'favorite_properties': favorite_properties,
    })

@login_required
def add_favorite_property(request, property_id):
    property_to_add = Property.objects.get(id=property_id)
    request.user.userprofile.favorite_properties.add(property_to_add)
    return redirect('profile')  # Redirect to profile after adding
