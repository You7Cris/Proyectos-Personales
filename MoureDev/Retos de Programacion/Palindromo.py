# def palabra(palabra):
#     if palabra.isalpha():
#         return True
#     else:
#         print("Tiene caracteres que no estan en el vocabulario")
#         return exit()

# def IsCasiPalindromo(palabra):

#     contador = 0
#     ordenar = list(palabra)
#     print(ordenar)
#     reversa = list(reversed(palabra))
#     print(reversa)
#     for i in range(len(ordenar)):
#         if ordenar[i] == reversa[i]:
#             print(ordenar[i])
#             pass
            
#         else:
#             contador = contador + 1
#     print(contador)
#     if contador >= 3:
#         respuesta = False
#     else:
#         respuesta = True
    
#     return print(f"{respuesta}")

# try:
#     palabra1 = input("Ingrese la palabra: ")
#     palabra(palabra1)
#     IsCasiPalindromo(palabra1)
# except ValueError:
#     print("Ocurrio un error al ingresar la palabra")
