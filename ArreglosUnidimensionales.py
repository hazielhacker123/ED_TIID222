print("\n========== CAPTURA 1: Consultar un elemento ==========")
numeros = [10, 20, 30, 40, 50]

print(numeros[2])


print("\n========== CAPTURA 2: Modificar un elemento ==========")
numeros = [10, 20, 30, 40, 50]

numeros[2] = 100

print(numeros)


print("\n========== CAPTURA 3: append() ==========")
numeros = [10, 20, 30, 40, 50]

numeros.append(60)

print(numeros)


print("\n========== CAPTURA 4: append([60, 70]) ==========")
numeros = [10, 20, 30, 40, 50]

numeros.append([60, 70])

print(numeros)
print(numeros[5][1])


print("\n========== CAPTURA 5: append(60) y append(70) ==========")
numeros = [10, 20, 30, 40, 50]

numeros.append(60)
numeros.append(70)

print(numeros)


print("\n========== EJEMPLO: imprimir numeros[5] ==========")
numeros = [10, 20, 30, 40, 50]

numeros.append([60, 70])

print(numeros[5])
print(numeros[5][0])


print("\n========== CAPTURA INSERT: insert(2, 25) ==========")
numeros = [10, 20, 30, 40]

numeros.insert(2, 25)

print(numeros)


print("\n========== CAPTURA 6: operador + ==========")
numeros = [10, 20, 30, 40]

numeros = numeros + [50]

print(numeros)


print("\n========== CAPTURA 7: + con varios elementos ==========")
numeros = [10, 20, 30, 40]

numeros = numeros + [50, 60, 70]

print(numeros)


print("\n========== EXTEND ==========")
numeros = [10, 20, 30]

otros_numeros = [40, 50, 60]

numeros.extend(otros_numeros)

print(numeros)
print(otros_numeros)


print("\n========== CAPTURA 8: len() ==========")
numeros = [10, 20, 30]

print(len(numeros))

numeros[len(numeros):] = [40]

print(numeros)


print("\n========== EJERCICIO 1: Calificaciones ==========")
calificaciones = [70, 85, 90, 65]

calificaciones.append(95)
print(calificaciones)

calificaciones.insert(2, 80)
print(calificaciones)


print("\n========== EJERCICIO 2: Colores ==========")
colores = ["Azul", "Amarillo", "Rosa"]

colores.extend(["Verde", "Morado", "Rojo"])

print(colores)
print("Negro")


print("\n========== EJERCICIO 3: Reto de posiciones ==========")
numeros = [10, 20, 30, 40]

numeros.insert(2, 95)
numeros.extend([50, 67])

print(numeros)
print(numeros[2])
print(numeros[6])