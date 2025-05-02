from django.shortcuts import render
from django.core.cache import cache

import requests, random

# Create your views here.
# def aleatorio(lista):
#     n = len(lista)-1
#     while n > 0:
#         r = random.randint(0,n)
#         aux = lista[r]
#         lista[r] = lista[n]
#         lista[n] = aux
#         n-=1


def obtener_personajes(request):


    URL_CHARACTERS = "https://rickandmortyapi.com/api/character"

    # headers = {
    #     "X-RapidAPI-Key": "bb2edfd33emsh0534ac5873a7a90p1e5bb6jsn97e9220f80ec",
    #     "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    # }
    try:
        response = requests.get(URL_CHARACTERS)

        if response.status_code == 200:

            characters = response.json()
            # aleatorio(characters.results)


            

        else:
            print(f"Error en la solicitud: {response.status_code}")
            characters = []
    except requests.RequestException as e:
        print(f"Error en la solicitud: {e}")
        characters = []



    URL_LOCATION = url = "https://rickandmortyapi.com/api/location"

    try:
        response = requests.get(URL_LOCATION)

        if response.status_code == 200:

            locations = response.json()

        else:
            print(f"Error en la solicitud: {response.status_code}")
            locations = []
    except requests.RequestException as e:
        print(f"Error en la solicitud: {e}")
        locations = []

    URL_EPISODES = url = "https://rickandmortyapi.com/api/episode"

    try:
        response = requests.get(URL_EPISODES)

        if response.status_code == 200:

            episodes = response.json()

        else:
            print(f"Error en la solicitud: {response.status_code}")
            episodes = []
    except requests.RequestException as e:
        print(f"Error en la solicitud: {e}")
        episodes = []

    # cache.delete()
    return render(request, 'api/api.html', {'characters':characters,'locations':locations, 'episodes':episodes})





