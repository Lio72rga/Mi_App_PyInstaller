#Ejemplo de variable Global

def mi_funcion():
    x = 5 # Variable local que enmascara a la variable global
    print(x)
mi_funcion() # Salida: 5
print(x) # Salida: 10