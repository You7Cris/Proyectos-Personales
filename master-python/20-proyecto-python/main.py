"""
Proyecto Python y MySQL:
- Abritr asistente
- Login o registro
- Si elegimos registro, creara un usuario en la bd
- Si elegimos login, identifica al usuario y nos preguntara
- Crear nota, mostrar notas, borrarlas
"""

from usuarios import acciones 
#import usuarios.acciones

print("""
    Acciones disponibles:
    - Registro
    - login
""")

hazEl = acciones.Acciones()
accion = input("¿Que quieres hacer?: ")

if accion == "registro":
    hazEl.registro()
    
elif accion == "login":
    hazEl.login()
