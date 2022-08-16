# Definir clases y estructuras de los formularios+

from django import forms
from django.core import validators # Libreria para validar diferentes tipos de datos

# Validators Django https://docs.djangoproject.com/en/4.0/ref/validators/

class FormArticle(forms.Form):

    title = forms.CharField(
        label = "Titulo",
        max_length=20,
        required =True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingresa el titulo',
                'class': 'titulo_form_article'
            }
        ),
        validators=[
            validators.MinLengthValidator(4 , 'El titulo es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9ñ ]*$', 'El titulo esta mal formado', 'invalid_title') #Ingresar caracteres de A - Z, a - z y 0 - 9 las veces que quiera
        ]
    )

    content = forms.CharField(
        label="Contenido",
        widget = forms.Textarea,
        validators=[
            validators.MaxLengthValidator(20, 'Has ingresado demasiado texto')
        ]
    )
    """
        attrs={
            'placeholder': 'Ingresa el texto del articulo',
            'class': 'contenido_form_article'
        }
    # permiten formatear o cambiar el formato que se va a mostrar # Una forma de ponerle estilos
    """

    content.widget.attrs.update({
        'placeholder': 'Ingresa el contenido del articulo',
        'class': 'contenido_form_article',
        'id': 'contenido_form'
    }) # Segunda forma

    public_options = [
        (1, 'Si'),
        (0, 'No')
    ]

    public = forms.TypedChoiceField(
        label="¿Publicado?",
        choices = public_options #pasar serie de opciones 
    )