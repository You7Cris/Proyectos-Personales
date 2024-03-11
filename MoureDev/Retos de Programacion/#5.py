#AREA DE UN POLIGONO
def poligono(a):
    a = int(a)
    if a == 1:
        lado = -1
        try:
            while lado < 0:
                lado = float(input("Ingrese el lado del cuadrado: "))
            
            area = lado * lado
           

        except ValueError:
            print("Error al ingresar el valor...")
    
        return print(f"El area del cuadrado es {area}")
    
    elif a == 2:
        base = -1
        altura = -1
        try:
            while base < 0 or altura < 0:
                base = float(input("Ingrese la base del triangulo: "))
                altura = float(input("Ingrese la altura del triangulo: "))

            area = (base * altura) / 2
            
        except ValueError:
            print("Error al ingresar el valor...")
        
        return print(f"El area del triangulo es: {area}")

    else:
        base = -1
        altura = -1
        try:
            while base < 0 or altura < 0:
                base = float(input("Ingrese la base del rectangulo: "))
                altura = float(input("Ingrese la altura del rectangulo: "))

            area = (base * altura) / 2
            return print(f"El area del rectangulo es: {area}")

        except ValueError:
            print("Error al ingresar el valor...")
    
    #return print(f"El area es: {area}")


opcion = -1
try:
    while int(opcion) < 0 or int(opcion) > 3:
        opcion = input("Ingrese\n1. Cuadrado\n2. Triangulo\n3. Rectangulo\nOpcion: ")

    poligono(opcion)

except ValueError:
    print("Error al ingresar los datos ...")