from django.contrib import admin

from .models import Arrivals, Ciudad, Departures, Gate, Remarks_arrivals, Remarks_departures

# Register your models here.

class CiudadAdmin(admin.ModelAdmin):
    readonly_fields =('created_at',)
    
class Remarks_arrivalsAdmin(admin.ModelAdmin):
    readonly_fields =('created_at',)
    
class ArrivalsAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'created_at', 'update_at')
    search_fields = ('lugar', 'user__username', 'flight_no' )
    
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id

        obj.save()
        
        
class GateAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',) 
    


class Remarks_departuresAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    
class DeparturesAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'created_at', 'update_at')
    search_fields = ('lugar', 'user__username', 'flight_no' )
    
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id

        obj.save()


# Cargar modelos en el panel
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Remarks_arrivals, Remarks_arrivalsAdmin)
admin.site.register(Arrivals, ArrivalsAdmin)
admin.site.register(Gate, GateAdmin)
admin.site.register(Remarks_departures, Remarks_departuresAdmin)
admin.site.register(Departures, DeparturesAdmin)



