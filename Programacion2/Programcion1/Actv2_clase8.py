#Utilizar la búsqueda de salto para encontrar un número en una lista 
# ordenada de manera eficiente.

import math

def busqueda_salto(lista, objetivo):
    longitud = len(lista)
    paso = int(math.sqrt(longitud))  # Determina el tamaño del bloque a saltar
    prev = 0

    # Encuentra el bloque donde el elemento puede estar presente
    while lista[min(paso, longitud) - 1] < objetivo:
        prev = paso
        paso += int(math.sqrt(longitud))
        if prev >= longitud:
            return -1

    # Realiza una búsqueda lineal en el bloque
    for i in range(prev, min(paso, longitud)):
        if lista[i] == objetivo:
            return i

    return -1

# Lista ordenada de números
numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]

# Número a buscar
objetivo = 17

# Llamada a la función de búsqueda de salto
resultado = busqueda_salto(numeros, objetivo)

if resultado != -1:
    print(f'El número {objetivo} se encuentra en la posición {resultado}.')
else:
    print(f'El número {objetivo} no se encuentra en la lista.')