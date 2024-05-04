from datetime import date

dia = date.today()
print(f"Hoy es: {dia}")

suma = 5 + 9

print("La suma es: ", suma , " Es la suma de estos dos numeros")

anio = 2024
print(anio + 1)
print(anio - 1)
print(anio / 2)
print(anio * 2)
print(anio ** 2)

print(4 ** 2)

parrafo = """
Mi nombre es Cristian Steven Gonzalez Arango
y soy ingeniero en sistemas

"""

miNombre = "Cristian Steven Gonzalez Arango"

print(parrafo)

presentacion = f"Mi nombre es {miNombre} y estamos en el año {anio}"

print(presentacion)

altura = 1.75

hayArepa = True
hayQueso = False

print('Puedo hacer arepa con queso?', hayArepa and hayQueso)
print('Puedo desayunar alguna cosa?', hayArepa or hayQueso)
print('No hay queso?', not hayQueso)

if hayArepa and hayQueso:
    print('Desayunar arepa con queso.')
else:
    print('Desayunar alguna otra cosa.')


# numero = int(input("Escriba un numero: "))

# if numero < 0:
#     print("El numero es negativo")
#     if numero > -10:
#         print("El numero esta entre -1 y -9")
#     else:
#         print("El numero es menor o igual a -10")
# elif numero < 10:
#     print("El numero es positivo y menor a 10")
# else:
#     print("El numero es positivo y mayor a 10")


numero = 3

if numero == 1.0 + 2.0:
    print('Son iguales')
else:
    print('No son iguales')

# JavaScript 
#  numero == 1 comparacion del valor intrinsico si es un char '1' y tengo un numero '1' va a devolver un True
# numero === 1 comparacion ya de igualdad que en el caso anterior deberia devolver False
print(abs(numero - 3.0))
if abs(numero - 3.0) == 0:
    print('Son iguales')
else:
    print('Diferentes')


# valorUsuario = int(input('Ingrese algo: '))
# valorUsuario = bool(valorUsuario)
# valorUsuario = str(valorUsuario)
# print(type(valorUsuario))

# Estructuras de datos

miListaCompras = ['500 cilantro','comprar 2 zanahorias','5 cebollas','1kg papas']

print(miListaCompras[0])
miListaCompras.insert(0,'Una Sandia')

miListaCompras.append('1lb de arroz')

for i in miListaCompras:
    print(i)

tabla_persona = [
    ['Diego','Moreno', 1997],
    ['Ana','Arias',2000],
    ['Marcela','Giraldo',1999],
    ['Gustavo','Arciniegas',2004]
]

print(tabla_persona[0][0])

for fila in tabla_persona:
    for columna in fila:
        print(columna)


for num in range(0,10,1):
    print(num, end=',')

print("###################")

contador = 0

while contador < 10:
    print(contador)

    contador += 1
    # contador = contador + 1

# Diccionario

persona = {
    'nombre' : 'Cristian',
    'edad' : 24,
    'altura': 1.75,
    'profesion': 'Ingeniero en sistemas',
    'telefono': '310 460 7480',
    'correo': 'cristan2110239@gmail.com'
}


print("Hola mundo")

