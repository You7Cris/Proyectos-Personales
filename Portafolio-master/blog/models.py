from datetime import datetime
from tabnanny import verbose
from django.db import models
import datetime
from django.db.models import Model

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo") 
    description = models.TextField(verbose_name="descripcion")
    image = models.ImageField(upload_to='blog/images', verbose_name="Imagen")
    date = models.DateField(datetime.date.today)
    
    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        
    