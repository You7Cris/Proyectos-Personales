from django.urls import path
from . import views

urlpatterns = [
    path('',views.obtener_personajes, name="api"),
]