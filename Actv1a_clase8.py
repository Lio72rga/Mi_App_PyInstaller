#Implementar la busqueda lineal en una lista de 
# numeros desordenados

def busqueda_lineal(lista, elemento):
    for i in range(len(lista)):
        if lista [i] == elemento:
            return i
    return -1
#Ejemplo de uso
numeros = [3, 7, 5, 9, 12, 21, 6, 2]
elemento_buscado = 21
indice = busqueda_lineal(numeros, elemento_buscado)
print(indice)