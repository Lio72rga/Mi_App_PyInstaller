#Busqueda lineal
#Implementar la busqueda lineal en una lista de numeros desordenados
def busqueda_lineal(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i #Devuelve el indice en el que se encontro el elemento
    return -1 #Si el elemento no se encuentra devuelve -1

#Ejemplo de uso
numeros = [2, 5, 8, 10, 3, 1]
elemento_buscado = 10
indice = busqueda_lineal(numeros, elemento_buscado)
print(indice) #Salida 3