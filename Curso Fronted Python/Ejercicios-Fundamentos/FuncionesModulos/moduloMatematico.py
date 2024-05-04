def proceso(opcion,n1,n2):
    if opcion == 1:
        resultado = n1 + n2
    elif opcion == 2:
        resultado = n1 - n2
    elif opcion == 3:
        resultado = n1 * n2
    elif opcion == 4:
        if n2 == 0:
            return print("No se puede dividir entre cero")
        else:
            resultado = n1 / n2
    else:
        exit()
    
    return print(f"El resultado es: {resultado}")


try:
    print("Programa para el modulo de operaciones...")
    opcion = -1
    while opcion < 0 or opcion > 4:
        print("1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n0.Salir")
        opcion = int(input("Ingrese la operacion que desea realizar: "))
    
    n1 = float(input("Ingrese el primer numero: "))
    n2 = float(input("Ingrese el segundo numero: "))
    proceso(opcion,n1,n2)


except ValueError:
    print("Datos incorrectps...")