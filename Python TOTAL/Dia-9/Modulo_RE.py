# expresiones regulares, permite realizar busquedas pero con una mayor complejidad

# [string] + '@' + [string] + '.com'

# Modulo RE = Regular expresions 
# patron para un numero = r' \d{3}-\d{3}-\d{4}

# caracteres especiales
#/d digito numerico  v\d.\d\d
#/w caracter alfanumerico \w\w\w-\w\w
#/s espacio en blanco numero\s\d\d
#/D NO numerico \D\D\D\D
#/W NO es alfanumerico \W\W\W solo acepta signos
#/S NO espacio en blanco \S\S\S\S

# cuantificadores
# + 1 o mas veces codigo_\d-\d+
#{n} se repite n veces \d-\d{4}
#{n, m} se repite de n a m veces \w{3,5}
#{n, } desde n hacia arriba -\d{4,}-
# * 0 o mas veces \w\s*\w
# ? 1 o 0  casas?

import re

texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horasa servicio de ayuda online"

palabra = 'ayuda' in texto
print(palabra)

patron = 'nada'

busqueda = re.search(patron, texto) # Solo busca una
#print(busqueda.span()) # Informacion de la ubicacion

#print(busqueda.start()) # Comienzo
#print(busqueda.end()) # Final

busqueda = re.findall(patron, texto) # Busca todas las veces que se encuentre

for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())

texto = "Llama al 564-525-6588 ya mismo"

patron = r'\d\d\d-\d\d\d-\d\d\d\d'
patron = r'(\d{3})-(\d{3})-(\d{4})'

resultado = re.search(patron, texto)

print(resultado)
print(resultado.group(1))

clave = input("Clave: ")

patron = r'\D{1}\w{7}'

chequear = re.search(patron, clave)

print(chequear)

texto = "No atendemos los lunes por la tarde"

buscar = re.search(r'lunes|martes',texto)
print(buscar)

buscar = re.findall(r'[^\s]+', texto)

print(buscar)

