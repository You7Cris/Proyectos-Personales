from turtle import title
from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article
from django.db.models import Q
from miapp.forms import FormArticle
from django.contrib import messages # Flash

# Create your views here.

#MVC = Modelo - Vista - Controlador 
#MVT = Modelo - Template (Vista dentro de Django) - Vista (Se conoce como controlador dentro de Django)

layout = """
<h1>Sitio Web con Django | Cristian Gonzalez</h1>
<hr/>
<ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
    <li>
        <a href="/hola-mundo">Hola Mundo</a>
    </li>
    <li>
        <a href="/pagina-pruebas">Pagina de pruebas</a>
    </li>
    <li>
        <a href="/contacto">Contactos</a>
    </li>
</ul>
</hr>
"""


def index(request):

    """

    html = "
        <h1>Inicio</h1>
        <p>Años hasta el 2050:</p>
        <ul>
    "

    year = 2021
    while year <= 2050:
        if year % 2 == 0:
             html += f"<li>{str(year)}</li>"

        year += 1

    html += "</ul>"
    """

    year = 2021
    hasta = range(year, 2051)


    nombre = 'Cristian Gonzalez'

    lenguajes = ['JavaScript', 'Python', 'PHP', 'C++']


    #return HttpResponse(layout + html)
    # Metodo render sabe que tiene que buscar dentro de los templates
    return render(request, 'index.html', {
        'title': 'Inicio',
        'mi_variable': 'Soy un dato que esta en la vista',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years' : hasta
    })



def hola_mundo(request): #Request se tiene que pasar para las vistas
    #return HttpResponse(layout + """""")
    return render(request, 'hola_mundo.html')

def pagina(request, redirigir=0):

    if redirigir == 1:
        #return redirect('/contacto/Cristian/Gonzalez')
        return redirect('contacto', nombre="Cristian", apellidos="Gonzalez")

    # return HttpResponse(layout + """""")

    return render(request, 'pagina.html',{
        'texto': 'Este es mi texto',
        'lista': ['uno','dos','tres']
    })

"""
def contacto(request, nombre, apellidos):
    return HttpResponse(layout + f 
        <h1> Pagina de Contacto {nombre} {apellidos}</h1>
        <h3>Creado por Cristian Gonzalez</h3>
    )
"""

# Parametros opcionales
def contacto(request, nombre="", apellidos=""):
    html = ""

    if nombre and apellidos:
        html += "El nombre completo es: "
        html += f"<h3>{nombre} {apellidos}</h3>"

    return HttpResponse(layout+f"<h2>Contacto</h2>"+html)


def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public = public
    )

    articulo.save() # Crear mi articulo en la base de datos

    return HttpResponse(f"Usuario creado: {articulo.title} - {articulo.content}")


def save_article(request):

    #Metodo GET

    """
    if request.method == 'GET':

        title = request.GET['title']
        content = request.GET['content']
        public = request.GET['public']

        articulo = Article(
        title = title,
        content = content,
        public = public
        )

        articulo.save() # Crear mi articulo en la base de datos

        return HttpResponse(f"Usuario creado: {articulo.title} - {articulo.content}")

    
    else:
        
        return HttpResponse("<h2>No se ha podido crear el articulo</h2>")
    """
    # Metodo POST
    if request.method == 'POST':

        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']

        articulo = Article(
        title = title,
        content = content,
        public = public
        )

        articulo.save() # Crear mi articulo en la base de datos

        #return HttpResponse(f"Usuario creado: {articulo.title} - {articulo.content}")
        return redirect('articulos')

    
    else:
        
        return HttpResponse("<h2>No se ha podido crear el articulo</h2>")

def create_article(request):

    return render(request, 'create_article.html')

def create_full_article(request):

    if request.method == 'POST':

        formulario = FormArticle(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            title = data_form.get('title')
            content = data_form['content']
            public = data_form['public']

            articulo = Article(
                title = title,
                content = content,
                public = public
            )

            articulo.save()

            # Crear mensaje flash (sesion que solo se muestra una vez)

            messages.success(request, f'Articulo {articulo.id} guardado correctamente')

            return redirect('articulos')

            #return HttpResponse(title + ' ' + content + ' ' + str(public))
        """
        else:

            return redirect('articulos')
        """

    else: 
        formulario = FormArticle()

    return render(request, 'create_full_article.html',{
            'form': formulario
    })



def articulo(request):

    try:
        articulo = Article.objects.get(title="Primer articulo") #pk (primary key)
        response = f"Articulo: <br/> {articulo.id}. {articulo.title}"
    except:
        response = "<h1>Articulo no encontrado</h1>"

    return HttpResponse(response)

def editar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    
    articulo.title = "Batman"
    articulo.content = "Pelicula del 2017"
    articulo.public = True

    articulo.save()

    return HttpResponse(f"Articulo {articulo.id} actualizado: {articulo.title} - {articulo.content}")

def articulos(request):

    articulos = Article.objects.all() # Muestra todo lo de la base de datos
    #articulos = Article.objects.order_by('title') #Ordenar el listado
    #articulos = Article.objects.order_by('-title') #Ordenar de forma descedente
    #articulos = Article.objects.order_by('id')[:3] #Solo me muestre 3 elementos
    #articulos = Article.objects.order_by('id')[3:10] #Solo me muestre elementos del 3 al 10

    #articulos = Article.objects.filter() # Filter permite agregar condiciones
    # articulos = Article.objects.filter(title__exact="articulo") # Mostrar solo el que contenga el titulo articulo
    # articulos = Article.objects.filter(title__iexact="articulo") 
    # id__gt = 12 mayores a 12
    # id__lt = 12 menores o iguales a 11
    # title__contains = "articulos" (que contengan como titulo articulos)
    # Mostrar el articulo que contenga de titulo articulo independientemente si es en mayuscula o en minuscula 

    ##########

    """
    articulos = Article.objects.filter(
        title = "Articulo"
    ).exclude(
        public = True
    )
    """

    # articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE title='Spiderman' AND public=1") # Consulta SQL

    """
    articulos = Article.objects.filter(
        Q(title__contains = "2" ) | Q(title__contains = "3") 
    ) # Que tengan uno OR otro 
    """

    return render(request, 'articulos.html', {
        'articulos': articulos
    })

def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect('articulos')