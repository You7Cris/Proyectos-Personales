from cmath import log
import logging
from django.shortcuts import render, get_object_or_404
from arrivals_departures.models import Ciudad, Remarks_arrivals, Arrivals, Gate, Remarks_departures, Departures
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
def list_llegadas(request):
    
    # Sacar llegadas
    llegadas = Arrivals.objects.all()
    
    #Paginar
    #paginator = Paginator(llegadas, 7)
    
    return render(request, 'departures/list.html',{
        'title': 'Llegadas (Arrivals)',
        'arrivals': llegadas
    })
    
@login_required(login_url="login")
def city_llegadas(request, ciudad_id):
    
    city_llegadas = get_object_or_404(Ciudad, id=ciudad_id)
    
    llegadas = Arrivals.objects.filter(ciudades = ciudad_id)
    
    return render(request, 'cities/city_arrival.html',{
        'city_llegadas': city_llegadas,
        'arrival' : llegadas
    })
    
@login_required(login_url="login")
def list_salidas(request):
    
    salidas = Departures.objects.all()
    
    return render(request, 'arrivals/list.html',{
        'title' : 'Salidas (Departures)',
        'departures': salidas
    })
    
@login_required(login_url="login")
def city_salidas(request, ciudad_id):
    city_salidas = get_object_or_404(Ciudad, id=ciudad_id)
    
    salidas = Departures.objects.filter(ciudades = ciudad_id)
    
    return render(request, 'cities/city_departure.html',{
        'city_salidas' : city_salidas,
        'salidas' : salidas
    })
    
    

    
    


