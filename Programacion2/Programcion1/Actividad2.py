import time
from playsound import playsound

def contador_regresivo(segundos):
    while segundos > 0:
        minutos, segundos_restantes = divmod(segundos, 60)
        print(f"{minutos:02d}:{segundos_restantes:02d}", end="\r")
        time.sleep(1)
        segundos -= 1
    print("¡Tiempo terminado!")
    playsound('alarma.mp3')

try:
    tiempo_inicial = int(input("Introduce el tiempo en segundos: "))
    contador_regresivo(tiempo_inicial)
except ValueError:
    print("Por favor, introduce un número válido.")


