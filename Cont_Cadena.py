#Contador de cadena
#Solicitar al usuario que ingrese una cadena de text

cadena= input("Introduzca una cadena de texto: ")

#Solicitar al usuario la letra que decea contar
letra = input("Ingrese la letra que decea contar: ")

#Recorrer la cadena de texto y contar las apariciones de la letra
contador = cadena.count (letra)

#Imprime el resultado
print(f"La letra '{letra}' aparece {contador} veces en la cadena.")