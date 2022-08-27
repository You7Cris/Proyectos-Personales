from django.urls import path
from .views import CompanyView
from . import views

urlpatterns = [
    
    #path('', views.index, name="index"),
    #path('inicio/', views.index, name="inicio"),
    
    # Trabajar con archvios JSON 
    path('companies/', CompanyView.as_view(), name='companies_list'),
    path('companies/<int:id>',CompanyView.as_view(), name='companies_process'),
]
