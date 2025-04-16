from sympy.logic.boolalg import true
numeros = [3, 1, 4, 5, 2]
ordenada = sorted(numeros,reverse=True)
print(ordenada)

frutas = ["manzana", "banana", "pera"]  
frutas.sort(key=str.lower, reverse=true)
print(frutas)

numeros = [1, 2, 3, 2, 2, 4, 5, 2]
print(numeros.count(2))

frutas = ["manzana", "banana", "pera"]  
print(len(frutas))

numeros = [1, 2, 3, 2, 2, 4, 5, 2]
print(len(numeros))

notas =[7, 8, 9, 7, 10, 7, 6, 7]
frecuencia =notas.count(7)
total = len(notas)
porcentaje = (frecuencia / total)* 100
print(f"El 7 aparece {frecuencia} veces, el {porcentaje:.2f}% de la lista.")