

repetir = "s"

while repetir == "s":
    cola = []  

    while True:
        print("\n--- MENÚ DE COLAS ---")
        print("1. Insertar cola")
        print("2. Borrar en cola")
        print("3. Listar cola")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            try:
                numero = int(input("Escribe el número a insertar: "))
                cola.append(numero)  # se agrega al final de la cola
                print("Se insertó el", numero)
            except ValueError:
                print("Eso no es un número válido")

        elif opcion == "2":
            if len(cola) == 0:
                print("La cola está vacía, no hay nada que borrar")
            else:
                sacado = cola.pop(0)  # se saca el primer elemento
                print("Salió de la cola:", sacado)

        elif opcion == "3":
            if len(cola) == 0:
                print("La cola está vacía")
            else:
                print("Elementos de la cola (primero -> último):")
                for elemento in cola:
                    print(" ", elemento)

        elif opcion == "4":
            break

        else:
            print("Opción no válida, elige del 1 al 4")

    repetir = input("\n¿Desea ejecutar nuevamente el programa? (s/n): ").lower()

print("Fin del programa")