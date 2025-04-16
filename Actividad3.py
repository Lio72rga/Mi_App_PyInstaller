#Contador de cadena
#Solicitar al usuario que ingrese una cadena de texto

cadena= input("Introduzca una cadena de texto: ")

#Solicitar al usuario la letra que decea contar
letra = input("Ingrese la letra que decea contar: ")

#Iniciar el contador
contador = 0

#Recorrer la cadena de texto y contar las apariciones de la letra
for caracter in cadena:
    if caracter == letra:
        contador += 1

#Imprime el resultado
print(f"La letra '{letra}' aparece {contador} veces en la cadena.")