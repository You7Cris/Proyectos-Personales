try:
    diccionario = {
        "brillo":"iluminosidad",
        "orden":"organizacion",
        "bruja":"hechicera",
        "loco":"demente",
        "armonia":"calma"
    }

    palabra = input("Ingrese la palabra: ")
    palabra.lower()
    for i in diccionario:
        if i == palabra:
            valor = diccionario[i]
            print(f"El sinonimo de la palabra {palabra} es {valor}")
            break
    
except ValueError:
    print("Ingreso datos incorrectos...")
