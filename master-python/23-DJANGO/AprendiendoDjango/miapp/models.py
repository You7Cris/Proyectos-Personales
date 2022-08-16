from django.db import models

# Create your models here.

# Los modelos son pequeñas clases que van a generar objetos para trabajar dentro del proyecto de Django, modelos que permiten trabajar con las entidades del proyecto, los modelos representan una entidad.
# Va a tener la definicion de los campos.
# Un modelo representa una tabla de la bases de datos.

class Article(models.Model): 
    # Propiedades

    # models fields Django
    title = models.CharField(max_length=150, verbose_name="Titulo") # Tipo string   # campos
    content = models.TextField(verbose_name = "Contenido") # Guardar contenido grandes cantidades de informacion
    image = models.ImageField(default='null', verbose_name = "Imagen", upload_to = "articles")
    public = models.BooleanField(verbose_name = "¿Publicado?") # Guardar un True o False
    create_at = models.DateTimeField(auto_now_add=True, verbose_name = "Creado el" ) #Fecha automatica de guardado cuando se cree por primera vez
    update_at = models.DateTimeField(auto_now=True, verbose_name="Editado el") # Guardar la fecha de edicion

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"
        ordering = ['id']

    def __str__(self):

        if self.public:
            publico = "(publicado)"
        else:
            publico ="(privado)"

        return f"{self.title} {publico}"


class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    create_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"





