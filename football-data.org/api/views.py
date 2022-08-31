from django.shortcuts import render 
from .services import get_username




# Create your views here.

def hello_user(requests):
    return render(requests, 'layout.html', {
        'title': 'Partidos en vivo',
        'matches': get_username()
    })
