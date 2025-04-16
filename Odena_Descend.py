#Ejemplo de ordenacion descendente de una lista 
#Creamos una lista llamada original_list que contiene números
# desordenados: Usamos la función sorted(original_list, reverse=True)
# para ordenar los elementos de original_list en orden descendente.
# El argumento reverse=True indica que queremos ordenar en sentido 
# descendente.[3, 1, 4, 1, 5, 9, 2, 6].

original_list = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_descending = sorted(original_list, reverse=True)
print(sorted_descending) #Resultado: [9, 6, 5, 4, 3, 2, 1, 1]

#Uso de sort
original_list.sort(reverse=True)
print(ord) #Resultado: [9, 6, 5, 4, 3, 2, 1, 1] 