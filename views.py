from django.shortcuts import render
from .models import Headline

def home(request):
    headlines = Headline.objects.all()
    return render(request, 'home.html', {'headlines': headlines})
