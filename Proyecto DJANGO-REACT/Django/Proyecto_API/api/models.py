from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField(max_length=100)
    foundation = models.PositiveBigIntegerField()
    
    class Meta:
        verbose_name = 'Compañia'
        verbose_name_plural = 'Compañias'
    
    def __str__(self):
        return self.name