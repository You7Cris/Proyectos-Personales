serie = "N-02"

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe")

cliente = {'nombre':'Cristian',
           'edad': 24,
           'ocupacion':'Desarrollador'}

pelicula = {'titulo': 'Matrix',
            'ficha_tecnica': {'protagonista':'Keanu Reeves',
                              'director':'Lana y Lilly Wachowski'}}

elementos = [cliente, pelicula,'libro']

for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'ocupacion': ocupacion}:
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        case {'titulo': titulo,
              'ficha_tecnica': {'protagonista': protagonista,
                                'director': director}}:
            print("Es una pelicula")
            print(titulo, protagonista, director)
        case _:
            print("No se que es esto")