"""ProyectoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include # Se agrega el include para trabajar con los diferentes archivos urls
from django.conf import settings


# Separar las rutas en ficheros
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('sobre-nosotros/', views.about, name="about") #Ya no se va a utilizar
    path('', include('mainapp.urls')),
    path('', include('pages.urls')),
    path('', include('blog.urls'))
    # Cargar ficheros principales
]

# Ruta imagenes

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
