import os
while True:
    try:
        print("Calculadora de IMC")
        peso = float(input("Ingrese su peso en kg: "))
        altura = float(input("Ingrese su altura en mt: "))
        IMC = peso / (altura * altura)
        print("Su IMC es de: ",IMC)
        exit()
        
    except ValueError:
        print("Error al ingresar los datos")
        os.system("pause")
        