texto = input("Ingrese un texto: ")
letras = []
texto = texto.lower()
letras.append(input("Ingrese la primera letra: ").lower())
letras.append(input("Ingrese la segunda letra: ").lower())
letras.append(input("Ingrese la tercera letra: ").lower())

print("\nCANTIDAD DE LETRAS")
cantidad_letras = texto.count(letras[0])
print(f"""La letra {letras[0]} se encuentra {texto.count(letras[0])} veces
La letra {letras[1]} se encuentra {texto.count(letras[1])} veces
La letra {letras[2]} se encuentra {texto.count(letras[2])} veces 
      """)

print("\nnCANTIDAD DE PALABRAS")
palabras = texto.split() #Separa las palabras por espacios
print(f"Hemos encontrado {len(palabras)} en el texto")

print("\nLETRAS DE INICIO Y FIN")
letra_inicio = texto[0]
letra_fin = texto[-1] #Ultima letra
print(f"La letra inicial es {letra_inicio} y la letra final es {letra_fin}")

print("\nTEXTO INVERTIDO")
plabras = palabras[::-1]
texto_invertido = ' '.join(palabras)
print(f"Si ordenamos tu texto invertido va a decir: \n{texto_invertido}")

print("\nBUSCANDO LA PALABRA PYTHON")
buscar = "python" in texto
dic = {True: "Si", False: "No"}
print(f"La palabra 'Python' {dic[buscar]} se encuentra")

