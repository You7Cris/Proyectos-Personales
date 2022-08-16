"""
FOR 

for variable in elemento_iterable (lista, rango, etc)
    BLOQUE DE INSTRUCCIONES


"""

from ast import Num


contador = 0
resultado = 0

for contador in range(0,10):
    print("Voy por el "+str(contador))
    resultado = resultado + contador

print(f"El resultado es {resultado}")

#Ejemplo tablas de multiplicar
print("\n########## EJEMPLO #########")

Numero_usuario = int(input("¿De que numero quieres la tabla?: "))

if Numero_usuario < 1:
    Numero_usuario = 1

print(f"\n############## Tabla de multiplicar del numero {Numero_usuario} ######")

for numero_tabla in range(1,11):
    print(f"{Numero_usuario} x {numero_tabla} = {Numero_usuario * numero_tabla}")
else:
    print("Tabla finalizada")
