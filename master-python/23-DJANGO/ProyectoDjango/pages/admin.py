from django.contrib import admin
from .models import Pages

# Register your models here.

# Configuracion extra
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'update_at')
    search_fields = ('title','content') #Permita buscar por algo especifico (titulo)
    list_filter = ('visible' , ) # Filtro 
    list_display = ('title', 'visible', 'created_at') # Ver un listado con propiedades
    ordering = ('created_at',) # Ordenar por fecha de creacion

admin.site.register(Pages, PageAdmin) # Registrando el modelo

# Configuracion del panel de administracion
title = "Proyecto Django"
subtitle = "Panel de gestion"
admin.site.site_header=title
admin.site.site_title=title # Titulo de la pestaña del navegador
admin.site.index_title=subtitle



