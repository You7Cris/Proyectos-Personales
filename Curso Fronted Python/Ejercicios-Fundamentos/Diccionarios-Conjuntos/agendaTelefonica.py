import os

listaTelefonos = []   
        
while True:

    def agregar(listaTelefonos):

        print("Agregar numero")
        try:
            numero = int(input("Ingrese el numero: "))
            listaTelefonos.append(numero)
            print("Numero agregador exitosamente.....")

        except ValueError:
            print("Error al ingresar los datos...")
        

    def mostrar(listaTelefonos):

        contador = 1
        # print(len(listaTelefonos))
        if len(listaTelefonos) == 0:
            print("\n\nNo hay numeros para mostrar...")
        else:
            print("Mostrar numeros")
            for i in listaTelefonos:
                print(f"{contador}. {i}")
                contador += 1
            print("Lista cargada exitosamente...")

    def update(listaTelefonos):
        print("Actualizar un telefono")
        if len(listaTelefonos) == 0:
            print("\nNo hay numeros guardados...")
        else:
            mostrar(listaTelefonos)
            total = len(listaTelefonos)
            valor = 0
            try:
                while valor < 1 or valor > total:
                    valor = int(input("Que numero desea editar?: "))

                print(f"Vas a modificar el numero {listaTelefonos[valor-1]}")
                listaTelefonos[valor-1] = int(input("Nuevo numero: "))
                print("\nNumero actualizado exitosamente...")
            except ValueError:
                print("Error al ingresar los datos...")

    def delete(listaTelefonos):
        if len(listaTelefonos) == 0:
            print("\nNo hay numeros para eliminar...")
        else:
            contador = 1
            for i in listaTelefonos:
                print(f"{contador}. {i}")

            try:
                opcion = -1
                while opcion < 0 or opcion > len(listaTelefonos):
                    opcion = int(input("Que numero desea eliminar?: "))

                valor = opcion - 1
                del listaTelefonos[valor]
                print(f"Elemento eliminado exitosamente...")

            except ValueError:
                print("Error al ingresar los datos...")



    def refrescar():
        os.system("pause")
        os.system("cls")

    try:
        ############################# BLOQUE PRINCIPAL
        print("Programa de agenda telefonica")
        opcion = -1
        while opcion < 0 or opcion > 4:
            print("##########################")
            print("Bienvenido al Menu")
            print("1. Agregar\n2.Mostrar\n3.Editar\n4.Eliminar\n0.Salir")
            opcion = int(input("Opcion: "))
    
        if opcion == 0:
            exit()
        elif opcion == 1:
            agregar(listaTelefonos)
            refrescar()
        elif opcion == 2:
            mostrar(listaTelefonos)
            refrescar()
        elif opcion == 3:
            update(listaTelefonos)
            refrescar()
        else:
            delete(listaTelefonos)
            refrescar()



            
    except ValueError:
        print("Error al ingresar los datos...")
        os.system("pause")
    
    


