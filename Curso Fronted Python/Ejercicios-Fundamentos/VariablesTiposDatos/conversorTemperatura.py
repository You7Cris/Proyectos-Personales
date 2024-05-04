opcion = -1
try:
    while opcion < 0 or opcion > 2:
        print("Ingrese \n1.Convertir Farhenheit a Celsius\n2.Convertir Celsius a Fahrenheit\n0.Salir")
        opcion = int(input("Opcion: "))
    
    temperatura = float(input("Ingrese la temperatura: "))
    if opcion == 0:
        exit()

    elif opcion == 1:
        conversionCelsius = (5 / 9.8) * (temperatura - 32)
        print(f"La temperatura es: {conversionCelsius} Celsius")
    
    else:
        conversionCelsius = (1.8 * temperatura) + 32
        print(f"La temperatura es: {conversionCelsius} Farhenheit")

except ValueError:
    print("Error al ingresar los datos...")
