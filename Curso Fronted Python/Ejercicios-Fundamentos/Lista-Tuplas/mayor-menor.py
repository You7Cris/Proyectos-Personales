try:
    lista = [23,45,67,89,15,78,56,34,23,67,89,12]
    mayor = 0
    menor = 99999
    for i in lista:
        if i > mayor:
            mayor = i
        elif i < menor:
            menor = i
    
    print(f"El mayor numero de la lista es: {mayor}")
    print(f"El numero menor de la lista es: {menor}")

except ValueError:
    print("Error al ingresar los datos...")

    