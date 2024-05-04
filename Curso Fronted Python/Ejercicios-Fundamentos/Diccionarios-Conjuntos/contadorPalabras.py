try:
    print("Contador de palabras en Python")
    palabra = input("Ingrese una frase: ")
    palabra = palabra.lower()
    frase = ''
    lista = []
    contador = 0
    contador_palabra = len(palabra)
    for i in palabra:
        contador += 1
        if contador == contador_palabra:
            frase = frase + i
            lista.append(frase)
        elif i == ' ':
            lista.append(frase)
            frase = ''
        else:
            frase = frase + i
    
    lista = set(lista)
    # Contador por palabra
    for i in lista:
        contador = 0
        for j in lista:
            if i == j:
                contador += 1
        
        print(f"La palabra '{i}' se encuentra {contador} veces")

    print(lista)
            
    print(palabra)


except ValueError:
    print("Error al ingresar los datos...")