"""
Ejercicio 10.
El programa tiene que pedir la nota de 15 alumnos y sacar por panmtalla cuantos han aprobado y cuantos han suspendido.

"""
import os

aprobados = 0
reprobados = 0


for i in range (0,15):
    nota = -1
    while nota < 0 or nota > 5:
        nota = float(input(f"Ingrese la nota del estudiante {i+1}: "))
    else:
        print("Nota guardada con exito...")
    if nota >= 3:
        aprobados += 1
    else:
        reprobados += 1

    os.system("pause")
    os.system("cls")

print(f"Los estudiantes que aprobaron fueron {aprobados}")
print(f"Losa estudiantes que reprobaron fueron {reprobados}")
    

