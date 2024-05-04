def USD(opcion,valor):
    if opcion == 1:

        resultado = valor * 3800
    else:
        resultado = valor * 0.94
    
    return print(f"El valor es de : {resultado}")



def PesoColombiano(opcion, valor):
    if opcion == 1:
        resultado = valor * 0.00026
    else:
        resultado = valor * 0.00024
    
    return print(f"El valor es de: {resultado}")

def EURO(opcion, valor):
    if opcion == 1:
        resultado = valor * 1.06
    else:
        resultado = valor * 4161.92
    return print(f"El valor es de: {resultado}")

try:
    print("Conversion de divisas")
    opcion = -1
    while opcion < 0 or opcion > 3:
        print("Divisas:\n1.USD\n2.Peso Colombiano\n3.EURO\n0.Salir")
        opcion = int(input("Opcion: "))
    
    valor = float(input("Ingrese el valor a convertir: "))
    opcion2 = -1
    if opcion == 1:
        while opcion2 < 1 or opcion2 > 2:
            print("Ingrese la divisa a la que desea convertir")
            print("1. Peso Colombiano\n2.EURO")
            opcion2 = int(input("Opcion: "))
        
        USD(opcion2, valor)
    elif opcion == 2:
        while opcion2 < 1 or opcion2 > 2:
            print("Ingrese la divisa a la que desea convertir")
            print("1. USD\n2.EURO")
            opcion2 = int(input("Opcion: "))
        
        PesoColombiano(opcion2, valor)
    elif opcion == 3:
        while opcion2 < 1 or opcion2 > 2:
            print("Ingrese la divisa a la que desea convertir")
            print("1. USD\n2.Peso Colombiano")
            opcion2 = int(input("Opcion: "))
        
        EURO(opcion2, valor)

        
        
    else:
        exit()

except ValueError:
    print("Error al ingresar los datos...")