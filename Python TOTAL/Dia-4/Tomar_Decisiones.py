if True:
    print('Es correcto')


mascota = 'perro'

if mascota == 'gato':
    print("Tienes un gato")
elif mascota == 'perro':
    print("Tienes un perro")
else:
    print("No se que animal tienes")

edad = 16
calificacion = 9
if edad < 18:
    print("Eres menor de edad")
    if calificacion >= 7:
        print("Aprobaste el curso")
    else:
        print("No aprobaste")
else:
    print("Eres adulto")