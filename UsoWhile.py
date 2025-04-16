#Bucle While

import math

numero = int(input("Ingrese un numero: "))

while numero < 0:
    print("Erro -> deberia ser un numero positivo")
    numero = int(input("Ingrese un numero: "))

print(f"\n Su Raiz cuadrada es: {(math.sqrt(numero)):.2f}")