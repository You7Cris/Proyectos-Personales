# * Crea un programa que cuente cuantas veces se repite cada palabra
#  * y que muestre el recuento final de todas ellas.
#  * - Los signos de puntuación no forman parte de la palabra.
#  * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
#  * - No se pueden utilizar funciones propias del lenguaje que
#  *   lo resuelvan automáticamente.


palabra = input("Ingrese una frase para encontrar cuantas veces aparece esa palabra: ")
palabras = []
separacion = ""

palabra.lower() # Transformar todo en minuscula

longitud = 0
for i in palabra:
    longitud = longitud + 1
    #print(longitud)

    if (i == " "):
        #print(len(palabra))
        #print(longitud)
        palabras.append(separacion)
        separacion = ""
    if (i != " "):
        separacion = separacion + i
        #print(separacion)
    if (longitud) == len(palabra):
        palabras.append(separacion)

#print(palabras) # Lista de las palabras
palabras_texto = len(palabras)

for i in palabras:
    contador = 0
    for j in palabras:
        if i == j:
            contador = contador + 1
        else:
            pass

    print(f"[{i}] se encuentra: {contador} en el texto")    

#print(palabras_texto)

        




