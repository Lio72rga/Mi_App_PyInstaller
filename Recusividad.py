#Ejemplo de Recusividad en Python
"""1. Caso base:
Es el punto de terminación de la recursión. Define una condición
que se evalúa dentro de la función recursiva y determina
cuándo se debe detener la llamada recursiva. El caso base evita
que la función se llame infinitamente y asegura que la recursión
se detenga en algún momento.
2. Caso recursivo:
Es la parte donde la función se llama a sí misma para resolver
un problema más pequeño o similar al original. En cada
llamada recursiva, el problema se simplifica o se reduce en
tamaño hasta que se alcance el caso base.
"""

def contar_hasta_cero(n):
    if n <= 0: # Caso base
        print("¡Boom!")
    else: # Caso recursivo
        print(n)
        contar_hasta_cero(n - 1) # Llamada recursiva
        
contar_hasta_cero(5)