import numpy as np

# Crear un array multidimensional con numpy
array_multidimensional = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])

# Mostrar el array
print("Array original:")
print(array_multidimensional)

# Calcular la suma de los elementos
suma = np.sum(array_multidimensional)
print(f"\nLa suma de todos los elementos es: {suma}")

# Multiplicar todos los elementos por un escalar
escalar = 2
array_multidimensional *= escalar
print(f"\nArray después de multiplicar por {escalar}:")
print(array_multidimensional)