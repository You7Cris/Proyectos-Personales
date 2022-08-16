from django.shortcuts import render
from .models import Pages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url = "login")
def page(request, slug): # recibir todos los datos de la peticion
    
    page = Pages.objects.get(slug=slug)
    
    
    return render(request, "pages/page.html",{
        "page": page
    })
