import random

try:
    print("Juega piedra papel o tijeras contra la PC...")
    contadorG = 0
    contador = 0
    contadorPc = 0
    while contadorG != 3:
        opcion = -1
        while opcion < 0 or opcion > 3:
            print("1. Piedra\n2.Papel\n3.Tijeras")
            opcion = int(input("Opcion: "))
            opcionPc = random.randint(1,3)
        
        print("--------------")
        print(f"Opcion Jugador: {opcion}\nOpcion PC: {opcionPc}")
        if opcion == opcionPc:
            print("Empate")
        
        elif opcion == 1 and opcionPc == 2:
            print("Papel le gana a Piedra")
            print("Punto para PC")
            contadorPc += 1
        
        elif opcion == 1 and opcionPc == 3:
            print("Piedra le gana a Tijeras")
            print("Punto para Jugador")
            contador += 1
        
        elif opcion == 2 and opcionPc == 1:
            print("Papel le gana a piedra")
            print("Punto para jugador")
            contador += 1
        
        elif opcion == 2 and opcionPc == 3:
            print("Tijera corta Papel")
            print("Punto para PC")
            contadorPc += 1
        
        elif opcion == 3 and opcionPc == 1:
            print("Piedra rompe Tijeras")
            print("Punto para PC")
            contadorPc += 1
        
        elif opcion == 3 and opcionPc == 2:
            print("Tijera corta Papel")
            print("Punto para Jugador")
            contador += 1
        
        if contador > contadorPc:
            contadorG = contador
        else:
            contadorG = contadorPc
        
        print(f"Puntos para jugador: {contador}")
        print(f"Puntos para PC: {contadorPc}")
        print("\n------------------------------")
    
    if contador == 3:
        print("GANO JUGADOR!!!")
    else:
        print("GANO PC!!!")
        
except ValueError:
    print("Error al ingresar los valores...")