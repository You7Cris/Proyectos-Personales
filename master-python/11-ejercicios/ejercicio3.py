"""
Ejercicio 3. Programa que compruebe si una variable esta vacia y si esta vacia, rellenarla con texto en minusculas y mostrarlo en mayusculas.

"""

from cgitb import text


texto = ""

if len(texto.strip()) <= 0:

    # mostrar el texto
    texto = "hola soy un texto en minusculas"
    print(texto.upper()) #Convertir a mayusculas


else:
    print(f"La variable tiene contenido {texto}")
