# crear o mover archivos
# enumerar archivos
# crear rutas basados en strings

from pathlib import Path

base = Path.home() # Devuelve la ruta principal
print(base)

guia = Path(base, "Barcelona", "Sagrada_Familia.txt")
print(guia)

guia2 = Path(base, "Europa", "España", Path("Barcelona", "Sagrada_Familia.txt"))
guia3 = guia2.with_name("La_Pedrera.txt")

print(guia2)
print(guia3)

print(guia2.parent.parent.parent)

guia4 = Path(Path.home(),"Europa")

for txt in Path(guia).glob("**/*.txt"): # incluye carpetas y subcarpetas que encuentre .txt
    print(txt)

guia5 = Path("Europa","España","Barcelona","Sagrada_Familia.txt")
en_europa = guia.relative_to(Path("Europa")) # devuelve un nuevo objeto Path 
en_espania = guia.relative_to(Path("Europa", "España")) 

print(en_europa) # mostraria \España\Barcelona\Sagrada_Familia.txt
print(en_espania) # Mostraria Barcelona\Sagrada_Familia.txt


