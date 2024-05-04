import os, random

def adivinaNumero():
    print("Adivina el numero generado por la PC")
    print("Generando numero........")
    os.system("pause")
    numero = random.randint(0,21)
    print("Es un numero entre 1 y 20, cuentas con 5 vidas")
    vidas = 5
    while vidas != 0:
        try:
            numUser = 0
            while numUser < 1 or numUser > 20:
                numUser = int(input("Ingrese el numero: "))

                if numUser < 1 or numUser > 20:
                    print("El rango es entre 1 y 20")
                    os.system("pause")
                    os.system("cls")

            if numUser == numero:
                print("Felicidades, adivinaste el numero!!!")
                break
            elif numUser > numero:
                print("El numero es menor")
            else:
                print("El numero es mayor")

            vidas = vidas - 1
            print(f"Te quedan {vidas} vidas")
            print("---------------------")


        except ValueError:
            print("Error al ingresar los datos..")
    
    if vidas > 0:
        return print("Ganaste el juego!!")
    else:
        return print("Perdiste el juego!!")
    
def pcAdivina():
    print("El PC intentara adivinar un numero")
    print("Piensa en un numero entre el 1 y el 20....")
    os.system("pause")
    print("Estas listo?, la PC solo tendra 5 vidas")
    os.system("cls")
    vidas = 5
    menor = 1
    mayor = 20
    lista = []
    contador = 1
    while vidas != 0:
        numero = random.randint(menor,mayor)
        print(f"Es el numero {numero}?")
        try:
            opcion = -1
            while opcion < 1 or opcion > 2:
                print("1. Si\n2. No")
                opcion = int(input("Opcion: "))
                if opcion == 1:
                    return print("Lo lograste PC...")
                else:
                    a = -1
                    while a < 1 or a > 2:
                        print("Es mayor o menor?")
                        print("1. Mayor")
                        print("2. Menor")
                        a = int(input("Opcion: "))
                    
                    lista.append(numero)
                    if contador == 1:
                        if a == 1:
                            menor = numero
                            mayor = 20
                        else:
                            mayor = numero
                            menor = 1
                    else:
                        if a == 1:
                            for i in lista:
                                if i > numero:
                                    menor = numero
                                else:
                                    menor = i
                        else:
                            for i in lista:
                                if i > numero:
                                    mayor = numero
                                else:
                                    mayor = i

            vidas = vidas - 1
            contador += 1
            print(f"Te quedan {vidas} PC")
            if vidas == 0:
                return print(f"Se termino el juego, perdiste!!")
                
        except ValueError:
            print("Error al ingresar los datos...")
    




    
while True:

    try:
        print("##########################")
        print("Juego del numero aleatorio")
        print("##########################")
        opcion = -1
        while opcion < 0 or opcion > 2:
            print("Seleccione el juego que desea jugar\n1.Adivinar numero\n2.El PC advine tu numero\n0.Salir")
            opcion = int(input("Opcion: "))
        
        if opcion == 1:
            adivinaNumero()
            os.system("pause")
            os.system("cls")
        elif opcion == 2:
            pcAdivina()
            os.system("pause")
            os.system("cls")
        else:
            exit()

    except ValueError:
        print("Error al ingresar los datos...")