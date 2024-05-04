try:

    print("Fibonacci")
    numero = int(input("Ingrese un numero para realizar la secuencia de fibonacci: "))
    inicio = 0
    final = 1
    for x in range(1,numero):
        if x == 1:
            resultado = final
        else:
            resultado = inicio + final
            inicio = final
            final = resultado
        
        print(final)
        
except ValueError:
    print("Error al ingresar los datos...")