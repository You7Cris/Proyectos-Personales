"""
Modulos: Son funcionalidadres ya hechas para reutilizar.
En python ya hay muchos modulos.
https://docs.python.org/3/py-modindex.html

Podemos conseguir modulos que ya vienen en el lenguaje,
modulos en internet, y tambien podemos crear nuestros modulos.
"""

#Importar modulo propio

#import mimodulo
#from mimodulo import holaMundo
from mimodulo import * #Importar todo lo del modulo 

#print(mimodulo.holaMundo("Cristian Gonzalez"))
#print(mimodulo.calculadora(5,7,True))

print(holaMundo("Cristian Gonzalez"))
print(calculadora(9, 7, True))


# Modulo de fechas
import datetime 

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.hour)
print(fecha_completa.day)
print(fecha_completa.month)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print("Mi fecha personalidada ",fecha_personalizada)

print(datetime.datetime.now().timestamp())

# Modulo de matematicas

import math

print("Raiz cuadrada de 10: ", math.sqrt(10))

print("El valor del numero pi: ",float(math.pi))

print("Redondear: ",math.ceil(6.67875))
print("Redondear: ",math.floor(6.67875)) #Redondear al numero bajo

#Modulo randow 
import random

print("Numero aleatorio entre 15 y 67: ", random.randint(15,67)) #Valores entre 15 y 67





