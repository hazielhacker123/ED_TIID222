##Declarando un arreglo
numeros = [10, 20, 30, 40, 50]

#Imprimimos un elemento en especial del arreglo
print(numeros[2])

#Reasigacion del valor de la posicion 

numeros[3] = 35
print(numeros)

#Se agrega un nuevo valor al final del arreglo
numeros.append(60)
print(numeros)


#Eliminamos un valor en el arreglo
numeros.remove(35)
print(numeros)


#Eliminamos un valor del arreglo usando la posición
numeros.pop(4)
print(numeros)


#

fruta = ['Manzana', 'Fresa', 'Sandía', 'Mango', 'Melon', 'Platano']

fruta.pop(4)
print(fruta)

fruta.remove('Manzana')
print(fruta)

arreglo = []

print(arreglo)

n = int(input('Ingrese el tamaño del arreglo: '))
print(n)


for i in range(n):
    dato = int(input('Ingrese un numero'))
    arreglo.append(dato)

print('El arreglo es: ', arreglo)


n = int(input('Ingrese el tamaño del arreglo: '))

arreglo = [0] * n
for i in range(n):
    dato = int(input('Ingrese un numero: '))
    arreglo[i] 








n = 15  

arreglo = [0] * n


for i in range(n):
    dato = int(input('Ingrese un número entero comprendido entre 0 y 500: '))

  
    while dato < 0 or dato > 500:
        print('Error: el número debe estar entre 0 y 500.')
        dato = int(input('Ingrese un número entero comprendido entre 0 y 500: '))

    arreglo[i] = dato


print('\nArray original:')
for num in arreglo:
    print(num, end=' ')

cincuerizado = []

for num in arreglo:
    if num % 5 == 0:
        cincuerizado.append(num)
    else:
        siguiente_multiplo = num + (5 - num % 5)
        cincuerizado.append(siguiente_multiplo)


print('\n\nArray cincuerizado:')
for num in cincuerizado:
    print(num, end=' ')