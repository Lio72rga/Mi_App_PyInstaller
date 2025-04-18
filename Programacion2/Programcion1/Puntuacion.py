#Calificación de un estudiante: Imagina que eres un profesor y deseas
#calcular las calificaciones finales de tus estudiantes en función de sus
#puntajes en un examen. La calificación final se asignará de la siguiente manera:

#➔ Si el puntaje es mayor o igual a 90, la calificación es "A".
#➔ Si el puntaje está entre 80 y 89, la calificación es "B".
#➔ Si el puntaje está entre 70 y 79, la calificación es "C".
#➔ Si el puntaje está entre 60 y 69, la calificación es "D".
#➔ Si el puntaje es menor que 60, la calificación es "F".

#Definimos puntuacion
puntuacion = int(input("Ingrese la puntuacion: "))

#determinar categoria para nota final

if puntuacion >= 90:
    print("La calificacion final es: A")
if puntuacion >= 80 and puntuacion <= 89:
    print("La calificacion final es: B")
if puntuacion >= 70 and puntuacion <= 79:
    print("La calificacion final es: C")
if puntuacion >= 60 and puntuacion <= 69:
    print("La calificacion final es: D") 
if puntuacion < 60:
    print("La calificacion final es: F")
