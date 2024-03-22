
#  * Crea un programa que invierta el orden de una cadena de texto
#  * sin usar funciones propias del lenguaje que lo hagan de forma automática.
#  * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

# Forma de hacerlo

palabra = input("Ingrese una palabra: ")
palabra_invertida = []

# for i in palabra:
#     palabra_invertida.append(i)

# palabra_invertida.reverse()
# palabra_invertida = "".join(palabra_invertida)
# print(palabra_invertida)

# Sin funciones

print(palabra[::-1])


