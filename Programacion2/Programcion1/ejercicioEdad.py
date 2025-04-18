#Verificacion de edad para ver una pelicula clasificacion PG-13
#suponngamos que estas desarrollando un programa para un cine
#y deseas asegurarte de que losespectadores sean lo suficientemente mayores para
# ver una película Debes solicitar la edad del espectador y permitirel acceso 
# solo si tienen al menos 13 años.

Edad_espectador = int(input("Ingrese la edad: "))

#Mensaje de acceso de edad

if Edad_espectador >= 13:
    print("Acceso Permitido !!!")


else:
    print("Lo siento! , no puede acceder a ver esta pelicula")
