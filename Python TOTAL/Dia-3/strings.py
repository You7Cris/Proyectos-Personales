# upper() - pasar a mayusculas
# lower() - pasar a minusculas
# split() - separalo en partes (listas)
# join() - unir items usando separador
# find() - encontrar un sub-string
# replace() - reemplazar un substring

texto = "Este es el texto de Cristian"
resultado = texto.upper()
print(resultado)

resultado = texto[2].upper()
print(resultado)

resultado = texto.lower()
print(resultado)

resultado = texto.split()
print(resultado)

resultado = texto.split("t") #Separa la lista hasta que encuentra la letra t
print(resultado)

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])
print(e)

resultado = texto.find("s") # Buscar find() permite buscar algo que puede que no se encuentre.
print(resultado)

resultado = texto.replace("Cristian","todos")
print(resultado)

resultado = texto.replace("e","x")
print(resultado)