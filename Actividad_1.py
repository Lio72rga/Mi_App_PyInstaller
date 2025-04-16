#Solicitar al usuario que ingrese un numero entre 1 y 100
def solicitar_numero():
    while True:
        try:
            numero = int(input("Por favor, ingrese un número entre 1 y 100: "))
            if 1 <= numero <= 100:
                print(f"El número ingresado es: {numero} y esta en el rango solicitado")
                break
            else:
                print("El número debe estar entre 1 y 100. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

solicitar_numero()
