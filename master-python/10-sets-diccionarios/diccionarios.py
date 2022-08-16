"""
Diccionario es un tipo de dato que almacena un conjunto de datos.
En formato <clave> valor.
Es parecido a un array asociativo o un objeto json.
"""

persona = {
    "nombre": "Victor",
    "apellidos": "Robles",
    "web": "victorroblesweb.es"
}

print(type(persona))
print(persona["apellidos"])

#Lista con diccionario

contactos = [
    {
        'nombre': 'Cristian',
        'email': 'cristian@gmail.com'
    },
    {
        'nombre': 'Luis',
        'email': 'luis@luis.com'
    },
    {
        'nombre': 'Salvador',
        'email': 'savador@gmail.com'
    }

]

contactos[0]['nombre'] = "Antoñito"
print(contactos[0]['nombre'])

print("\nListado de contactos: ")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("---------------------------------------------------")
