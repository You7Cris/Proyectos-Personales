try:
    print("Contador de vocales")
    vocales = ['a','e','i','o','u']
    palabra = input("Ingresa la palabra: ")
    palabra.lower()
    contador = 0

    for i in palabra:
        for j in vocales:
            if i == j:
                contador += 1

    print(f"Esta palabra tiene {contador} vocales")

except ValueError:
    print("Error al ingresar los datos...")