dia_semana = int(input("Ingrese un numero del 1 al 7 que represente cada dia de la semana"))

if dia_semana == 1:
    print("Lunes")
elif dia_semana == 2:
    print("Martes")
elif dia_semana == 3:
    print("Miercoles")

elif dia_semana == 4:
    print("Jueves")
elif dia_semana == 5:
    print("Viernes")
elif dia_semana == 6:
    print("Sabado")
elif dia_semana == 7:
    print("Domingo")
else:
    if dia_semana> 7:
        print("Numero no valido ingrese un numero del 1 al 7")
    