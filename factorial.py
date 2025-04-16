"""2. Cálculo del factorial de un número utilizando recursión.
Escribe una función llamada "factorial" que tome un número entero
como parámetro y devuelva su factorial. El factorial de un número se
calcula multiplicando todos los números enteros desde 1 hasta el
número dado."""
#Factorial recusivo
#Caso Base, el factorial de 0 o 1 es 1
def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
    # Llamada recursiva: x * factorial de (x-1)
        return x *factorial (x - 1)
# Ejemplo de uso
numero = 5
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")
        