"""
Ejercicio 6. Mostrar todfas las tablas de multiplicar del 1 al 10.
Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 

"""

contador = 1

for contador in range (1,11):
    print("-----TABLA DEL NUMERO " + str(contador) + "------")
    for contador2 in range (1,11):
        print(f" {contador} x { contador2} = {contador * contador2}")
    else:
        print("Tabla terminada")