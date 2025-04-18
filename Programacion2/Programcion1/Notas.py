#Cree un programa que determine y muestre al alumno la nota

#suspenso => Notas: 0, 1, 2, 3, 4 y 5

#Aprobado => Nota: 6

#Buena => Nota: 7

#Notable => Nota: 8

#Sobresaliente => Notas: 9 y 10

nota_alumno = int(input("Ingresar nota del alumno (entre 0 y 10): "))

#Determinar categoria

if 0 <= nota_alumno <=5:
        categoria = "Suspenso"
elif nota_alumno == 6:
        categoria = "Aprobado"
elif nota_alumno == 7:
        categoria = "Buena"
elif nota_alumno == 8:
        categoria = "Notable"
elif 9 <= nota_alumno <= 10:
        categoria = "Sobresaliente"
else:
        categoria = "ES INVALIDA"

#MOSTRAR LA CATEGORIA DEL ALUMNO
print(F"La categoria de calificacion es: {categoria}")