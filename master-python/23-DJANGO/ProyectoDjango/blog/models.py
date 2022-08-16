from email.policy import default
from tabnanny import verbose
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

# Modelo de blog

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.CharField(max_length=250, verbose_name="descripcion")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
    def __str__(self):
        return self.name
    

class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name="Titulo")
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(default='null',verbose_name="Imagen", upload_to="articles")
    public = models.BooleanField(verbose_name="¿Publicado?")
    user = models.ForeignKey(User, verbose_name='Usuario', editable=False, on_delete=models.CASCADE) #Si se borra el usuario se borran todos los articulos por el CASCADE
    categories = models.ManyToManyField(Category, verbose_name="Categorias", blank=True, related_name = "articles" ) #Relacion de muchos a muchos, por defecto no sea obligatorio poner una categoria
    #category = models.ForeignKey #Relacion de 1 a 1
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateField(auto_now=True, verbose_name="Actualizado el")
    
    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        ordering = ['-created_at']
        
    def __str__(self):
        return self.title
    
# Gracias a ManyToMany tiene una relacion con Categoria 

    
