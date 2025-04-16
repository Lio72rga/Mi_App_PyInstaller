#Ejemplo de estructuras de decision anidadas en Python

#Definir la variable
edad = 25

#comenzar la estructura de decision anidada
if edad < 0:
    print("Edad invalida")
else:
    if edad < 18:
        print("Eres menor de edad")
    else:
        if edad  < 60:
            print("Eres mayor de edad")
        else:
            print("Eres adulto")
    