from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ciudad(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    
    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
    
    def __str__(self):
        return self.name
    
class Remarks_arrivals(models.Model):
    name = models.CharField(verbose_name="Comentarios de llegada", max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    
    class Meta:
        verbose_name = 'Comentario llegada'
        verbose_name_plural = 'Comentarios de llegada'
        
    def __str__(self):
        return self.name
    
    
class Arrivals(models.Model):
    time = models.TimeField(verbose_name="Hora")
    lugar = models.ManyToManyField(Ciudad, verbose_name="Lugar", blank=True, related_name="arrivals")
    user = models.ForeignKey(User, verbose_name='Usuario', editable=False, on_delete=models.CASCADE)
    flight_no = models.CharField(max_length=6, unique = True,verbose_name="Numero de vuelo")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateField(auto_now=True, verbose_name="Actualizado el")
    remarks = models.ManyToManyField(Remarks_arrivals,   verbose_name="Comentarios", blank=True, related_name="arrivals_remark")
    expected_time = models.TimeField(blank= True, null = True, verbose_name="Hora esperada")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    update_at = models.DateField(auto_now=True, verbose_name="Actualizado el")
    
    
    class Meta:
        verbose_name = 'Llegada'
        verbose_name_plural = 'Llegadas'
        
    def __str__(self):
        return self.flight_no 
    
class Gate(models.Model):
    name = models.CharField(max_length=3, verbose_name="porton")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    
    class Meta:
        verbose_name = 'Porton'
        verbose_name_plural = 'Portones'
        
    def __str__(self):
        return self.name
    
class Remarks_departures(models.Model):
    name = models.CharField(verbose_name="Comentarios", max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    
    class Meta:
        verbose_name = 'Comentario de salida'
        verbose_name_plural = 'Comentarios de salida'
        
    def __str__(self):
        return self.name
    
    
    
class Departures(models.Model):
    time = models.TimeField(verbose_name="Hora")
    lugar = models.ManyToManyField(Ciudad, verbose_name="Lugar", blank=True, related_name="departures")
    user = models.ForeignKey(User, verbose_name="Usuario", editable=False, on_delete=models.CASCADE)
    flight_no = models.CharField(max_length=6, unique= True, verbose_name="Numero de vuelo")
    gate = models.ManyToManyField(Gate, verbose_name="Porton",blank=True, related_name="departures_gate")
    remarks = models.ManyToManyField(Remarks_departures, verbose_name="Comentarios", blank=True, related_name="departures_remarks")
    expected_time = models.TimeField(blank= True, null=True, verbose_name="Hora esperada")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    update_at = models.DateField(auto_now=True, verbose_name="Actualizado el")
    
    class Meta:
        verbose_name = 'Salida'
        verbose_name_plural = 'Salidas'
        
    def __str__(self):
        return self.flight_no
    

    
