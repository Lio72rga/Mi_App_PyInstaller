"""1. Suma de los elementos de una lista
Escribir una función llamada "sumar_lista" que reciba como
parámetro una lista de números enteros y devuelva la suma de todos
los elementos de la lista.
"""
def sumar_lista(*args):

    total = sum(args)
    return total

result = sumar_lista(2, 4, 6, 8, 10, 15)
print(result) # Output: 45