#Definir funcion  de busqueda binaria
def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        valor_medio = lista[medio]

        if valor_medio == objetivo:
            return medio
        elif valor_medio < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1

# Lista ordenada de palabras
palabras = ["almendra", "banana", "cereza", "durazno", "frambuesa", "guayaba", "manzana", "naranja", "pera", "uva"]

# Palabra a buscar
objetivo = "manzana"

# Llamada a la función de búsqueda binaria
resultado = busqueda_binaria(palabras, objetivo)

if resultado != -1:
    print(f'La palabra "{objetivo}" se encuentra en la posición {resultado}.')
else:
    print(f'La palabra "{objetivo}" no se encuentra en la lista.')
