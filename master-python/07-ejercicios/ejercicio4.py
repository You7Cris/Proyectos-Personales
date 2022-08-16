"""
Ejercicio 4. Pedir dos numeros al usuario y hacer todas las operaciones basicas de una calculadora y mostrarla por pantalla.

"""

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

print(f"La suma de {numero1} + {numero2} = {numero1 + numero2}")
print(f"La resta de {numero1} - {numero2} = {numero1 - numero2}")
print(f"La multiplicacion de {numero1} * {numero2} = {numero1 * numero2}")
if numero2 == 0:
    print("No se puede realizar esta division")
else:
    print(f"La division de {numero1} / {numero2} = {numero1/numero2}")