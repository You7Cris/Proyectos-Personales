"""
FUNCIONES:
Una funcion es un conjunto de instrucciones agrupadas bajo un nombre concreto que pueden reutilizarse invocando a la funcion tantas veces como sea necesario.

def nombreDeMiFuncion(parametros):
    # BLOQUE / CONJUNTO DE INSTRUCCIONES

nombreDeMiFuncion(mi_parametro)

"""

# Ejemplo 1

from pickle import NONE


print("### EJEMPLO 1 ####")

# Definir funcion 

def muestraNombre():
    print("Cristian")
    print("Pineda")
    print("Adrian")
    print("Flaco")
    print("\n")

# Invocar funcion

muestraNombre()


# Ejemplo 2 : parametros
print("####### EJEMPLO 2 #####")

#nombre = "Cristian Gonzalez"

def mostrarNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("No eres mayor de edad")


#nombre = input("Ingresa tu nombre: ")
#edad = int(input("Ingresa tu edad: "))
nombre = "Cristian"
edad = 14


mostrarNombre(nombre, edad)
#mostrarNombre("Cristian Gonzalez")

# Ejemplo 3
print("#### EJEMPLO 3 #######")

def tabla(numero):
    print(f"Tabla de multiplicar del numero: {numero}")

    for contador in range(11):
        operacion = numero * contador
        print(f"{numero} x {contador} = {operacion}")

    print("\n")

tabla(3)
tabla(7)
tabla(12)

#Ejemplo 3.1

for numero_tabla in range(1,11):
    tabla(numero_tabla)

# Ejemplo 4

print("###### EJEMPLO 4 #####")

# Parametros opcionales

def getEmpleado(nombre, dni = None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    
    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Cristian Gonzalez",1112793921)

# Ejemplo 5 : parametros opcionales y return o devolver datos

print("\n##### EJEMPLO 5 #####")
def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"

    return saludo

print(saludame("Cristian"))

# Ejemplo 6
print("\n#### EJEMPLO 6 ####")

def calculadora(numero1, numero2, basicas = False):

    suma = numero1 + numero2 
    resta = numero1 - numero2
    multi = numero1 * numero2
    if numero2 == 0:
        division = "Error"
    else:
        division = numero1 / numero2

    cadena = ""

    cadena += "Suma: " + str(suma)
    cadena += "\n"
    cadena += "Resta: " + str(resta)
    cadena += "\n"
    cadena += "Multiplicacion: " + str(multi)
    cadena += "\n"
    cadena += "Division: " + str(division)

    return cadena

print(calculadora(5,0))

# Ejemplo 7
print("\n##### Ejemplo 7 #####")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(devuelveTodo("Cristian","Gonzalez"))

# Ejemplo 8: Funciones Lamdba

print("\n##### EJEMPLO 8 #####")

dime_el_year = lambda year: f"El año es {year}"

print(dime_el_year(2034))


