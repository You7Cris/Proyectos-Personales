
try:
    print("Factorial de un numero")
    numero = int(input("Ingrese el numero: "))
    factorial = 1
    # Ciclo for
    for i in range(numero,0,-1):
        factorial = factorial * i
    
    print(f"el factorial de {numero} es: {factorial}")

    factorial = 1
    valorreal = numero
    # Ciclo While:
    while numero!=0:
        factorial = factorial * numero

        numero = numero - 1
    
    print(f"El factorial de {valorreal} es: {factorial}")


except ValueError:
    print("Error al ingresar los datos...")