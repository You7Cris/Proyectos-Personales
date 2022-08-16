#Condicionales

# Condicional IF

# Ejemplo 1

print("########### EJEMPLO 1 ###########")

#color = "rojo"

color = input("Cual es mi color favorito?: ")

if color == "rojo":
    print("Color correcto")
else:
    print("Color incorrecto")


#Operadores de comparacion
"""
== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que
"""
#EJEMPLO 2
print("\n########### EJEMPLO 2 ###########")

#year = 2020
year = int(input("En que año estamos?: "))

if year >= 2021:
    print("Estamos en el 2022")
else:
    print("Es un año posterior  a 2021")

#EJEMPLO 3
print("\n########### EJEMPLO 3 ###########")

nombre = "Cristian"
ciudad = "Madrid"
continente = "Europa"
edad = 23
mayor_edad = 18

if edad >= mayor_edad:
    #Instrucciones
    print(f"{nombre} es mayor de edad")
    if continente != "Europa":
        print("El usuario no es Europeo")
    else:
        print(f"{nombre} es Europeo y de {ciudad}")
else:
    print(f"{nombre} no es mayor de edad")

#EJEMPLO 4
print("\n########### EJEMPLO 4 ###########")

#dia = int(input("Ingrese el dia de la semana: "))
dia = 2
"""
if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
        print("Es martes")
    else:
        if dia == 3:
            print("Es miercoles")
        else:
            if dia == 4:
                print("Es jueves")
            else:
                if dia == 5:
                    print("Es viernes")
                else:
                    if dia == 6:
                        print("Es sabado")
                    else:
                        if dia == 7:
                            print("Es domingo")
                        else:
                            print("Error")
"""

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
elif dia == 6 | dia == 7:
    print("Es fin de semana")
else:
    print("Error")

#Operadores logicos

"""
and Y
or O 
! negacion
not No
"""


#EJEMPLO 5
print("\n########### EJEMPLO 5 ###########")

edad_minima = 18
edad_maxima = 65
edad_real = 17

if edad_real >= 18 and edad_real <= 65: 
    print("Esta en edad de trabajar")
else:
    print("No esta en edad de trabajar")


#EJEMPLO 6
print("\n########### EJEMPLO 6 ###########")

pais = "Alemania"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un pais de habla hispana")
else:
    print(f"{pais} no es un pais de habla hispana")

#EJEMPLO 7
print("\n########### EJEMPLO 7 ###########")

pais = "España"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO es un pais de habla hispana")
else:
    print(f"{pais} SI es un pais de habla hispana")
