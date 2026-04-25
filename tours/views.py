from django.shortcuts import render
from .models import Tour

def home(request):
    tours = Tour.objects.all().order_by('-created_at')
    return render(request, 'tours/home.html', {'tours': tours})