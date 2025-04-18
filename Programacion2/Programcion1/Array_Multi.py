# Crear un array multidimensional
array_multidimensional = [
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
]

# Mostrar el array
for sub_array in array_multidimensional:
    for fila in sub_array:
        for elemento in fila:
            print(elemento, end=' ')
        print()
    print()

