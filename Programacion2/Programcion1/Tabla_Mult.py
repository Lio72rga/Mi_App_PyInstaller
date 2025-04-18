#Presentar las tablas de multiplicar del 1,2,3...,10

n = int(input("Ingrese un numero"))
for i in range(11):
    resultado = n*i
    print(n,"x",i,"=",resultado)