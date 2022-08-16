"""
Ejercicio 8. 
¿ Cuanto es el x porciento de x numero?

"""

numero = int(input("Ingrese el numero: "))
porcentaje = float(input("Ingrese el porcentaje que desea sacar de ese numero: "))

print(f"El {porcentaje}% de {numero} es {numero*(porcentaje/100)}")