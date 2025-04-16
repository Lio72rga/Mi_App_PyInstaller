#-crear un programa que permita ingresar un nombre y una 
#cantidad numerica para que asi despues el programa escriba este 
#nombre tantas veces como su cantidad ingresada. Utilizar la funcion Mientras.
nombre= input("Ingresar un nombre: ")
cantidad = int(input("Ingrese una cantidad numerica: "))

contador = 0
while contador < cantidad:
    print(nombre)
    contador+=1