"""
Ejercicio 5.
Crear una lista con el contenido de esta tabla:
ACCION  AVENTURA            DEPORTES
GTA     ASSASINS CREED      FIFA 21
COD     CRASH               PRO 21
PUBG    PRINCE OF PERSIA    MOTO GP 21

Mostrar esta informacion ordenada 
"""

lista = [ 
    {
        "categoria": "ACCION",
        "juegos": ["GTA", "Call of Duty", "PUBG"]
    },
    {
        "categoria": "AVENTURA",
        "juegos": ["Assasins", "CRASH", "Prince of Persia"]
    },
    {
        "categoria": "DEPORTES",
        "juegos": ["FIFA 21", "PRO 21", "MOTO GP 21"]
    }

]

for categoria in lista:
    print(f"-----------------{categoria['categoria']}-----------------")
    for juego in categoria['juegos']:
        print(juego)




