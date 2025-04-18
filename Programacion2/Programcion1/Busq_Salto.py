import math

def busqueda_salto(lista, elemento):
    tamaño_bloque = int(math.sqrt(len(lista)))
    bloque_actual = 0
    siguiente_bloque = tamaño_bloque
    
    while lista[min(siguiente_bloque, len(lista)) - 1] < elemento:
        bloque_actual = siguiente_bloque
        siguiente_bloque += tamaño_bloque
        if bloque_actual >= len(lista):
            return -1
    
    for i in range(bloque_actual, min(siguiente_bloque, len(lista))):
        if lista[i]== elemento:
            return i
    return -1

#Ejemplo de uso
numeros = [2, 5, 8, 10, 12, 15, 18, 20, 25, 30]
elemento_buscado = 15
indice = busqueda_salto(numeros, elemento_buscado)
print(indice) #Salida 5