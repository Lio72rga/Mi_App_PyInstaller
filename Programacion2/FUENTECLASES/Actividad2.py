# 1. Crear una tupla que contenga los números enteros del 1 al 20
numeros = tuple(range(1, 21))
print("Tupla con los números del 1 al 20:")
print(numeros)

# 2. Imprimir desde el índice 10 al 15 de la tupla
print("Elementos de índice 10 al 15:")
print(numeros[10:16])  # El índice final no se incluye

# 3. Mostrar la cantidad de veces que se encuentra un elemento en la tupla y en la lista
# Ejemplo: contar el número 10
numero_a_contar = 10
# Contar en la tupla
conteo_tupla = numeros.count(numero_a_contar)
print(f"El número {numero_a_contar} aparece {conteo_tupla} veces en la tupla.")

# Crear una lista a partir de la tupla para contar en ella
numeros_lista = list(numeros)
conteo_lista = numeros_lista.count(numero_a_contar)
print(f"El número {numero_a_contar} aparece {conteo_lista} veces en la lista.")

# 4. Convertir la tupla en una lista
print("Tupla convertida en lista:")
print(numeros_lista)

# 5. Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables
primer, segundo, tercero = numeros[:3]
print("Primeros tres elementos desempaquetados:")
print(f"Primero: {primer}, Segundo: {segundo}, Tercero: {tercero}")
