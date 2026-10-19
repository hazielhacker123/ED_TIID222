

repetir = "s"

while repetir == "s":
    pila = [] 

    while True:
        print("\n--- MENÚ DE PILAS ---")
        print("1. Insertar pila")
        print("2. Borrar en pila")
        print("3. Listar pila")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            try:
                numero = int(input("Escribe el número a insertar: "))
                pila.append(numero)  
                print("Se insertó el", numero)
            except ValueError:
                print("Eso no es un número válido")

        elif opcion == "2":
            if len(pila) == 0:
                print("La pila está vacía, no hay nada que borrar")
            else:
                sacado = pila.pop()  
                print("Salió de la pila:", sacado)

        elif opcion == "3":
            if len(pila) == 0:
                print("La pila está vacía")
            else:
                print("Elementos de la pila (arriba -> abajo):")
                for elemento in reversed(pila):
                    print(" ", elemento)

        elif opcion == "4":
            break

        else:
            print("Opción no válida, elige del 1 al 4")

    repetir = input("\n¿Desea ejecutar nuevamente el programa? (s/n): ").lower()

print("Fin del programa")