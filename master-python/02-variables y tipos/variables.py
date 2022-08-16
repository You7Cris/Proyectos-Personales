"""
Una variables es un contenedor de informacion que dentro se guardara un dato, se pueden crear muchas variables y que cada una tenga un dato distinto
"""

texto = "Master en Python"
texto2 = "Con Cristian Gonzalez"
numero = 24
decimal = 6.4

# Mostrar valores de las variables

print(texto,texto2)

print("Labios compartidos, labios divididos")

# Concatenacion

nombre = "Cristian"
apellidos = "Gonzalez"
web = "Crisweb.es"

print("Hola soy " + nombre + " " + apellidos + " - " + web)
#La f permite interpolar
print(f"{nombre} {apellidos} - {web}")
print("Hola me llamo {} {} y mi web es: {}".format(nombre,apellidos,web))
print(nombre, apellidos, web) #Aca no estamos concatenando