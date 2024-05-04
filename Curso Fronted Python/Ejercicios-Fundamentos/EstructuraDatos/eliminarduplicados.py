try:
    numeros = []
    numero = 0
    while numero <= 0:
        numero = int(input("Ingrese la cantidad de numeros que va a ingresar: "))
    
    for i in range(numero):
        dato = int(input("Ingrese un numero: "))
        numeros.append(dato)

    print(set(numeros))



except ValueError:
    print("Error al ingresar los datos...")