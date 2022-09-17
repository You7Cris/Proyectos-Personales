from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from arrivals_departures.models import Arrivals, Departures

# Create your views here.

def index(request):
    llegadas = Arrivals.objects.all()
    salidas = Departures.objects.all()
    return render(request, 'mainapp/index.html',{
        'title': 'Inicio',
        'llegadas': llegadas,
        'salidas': salidas
    })
    
def panel_administrativo(request):
    if request.user.is_authenticated:
        return redirect('/admin')
    
    else:
        return redirect('/admin')
    
    
def login_page(request):
    if request.user.is_authenticated:
        return redirect('/admin')
    
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password = password)
            
            if user is not None:
                login(request, user)
                
                return redirect('/admin')
            
            else:
                messages.warning(request, "No se ha identificado correctamente")
                
        return render(request, 'users/login.html',{
            'title': 'Ingresar'
        })
                
def logout_user(request):
    logout(request)
    return redirect('login')