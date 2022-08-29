from django.shortcuts import render
from .models import Project

# Create your views here.


def home(request):
    projects = Project.objects.all() # Proyectos consultados en la base de datos
    
    
    
    return render(request, 'home.html', {'projects': projects})
