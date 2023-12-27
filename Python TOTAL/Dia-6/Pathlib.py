from pathlib import Path, PureWindowsPath # Manipular rutas en cualquier sistema Operativo

carpeta = Path('D:/xampp/htdocs/Proyectos-Personales/Python TOTAL/Dia-6/prueba.txt')

print(carpeta.read_text())

print(carpeta.name) # Nombre del archivo
print(carpeta.suffix) # Terminacion (de que tipo es el documento)
print(carpeta.stem) # Nombre sin extension

if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Genial, existe!")

# PureWindowsPath transformar a una ruta dfe windows

ruta_windows = PureWindowsPath(carpeta)

print(ruta_windows)