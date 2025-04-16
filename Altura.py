




#ingresar datos

altura = float(input("Ingresar altura en centimetro"))

#calculamos

if altura <= 150:
    categoria = "Persona altura baja"
elif 151 <= altura <= 170:
    categoria = "Persona de altura media"
else:
    categoria = "Persona alta"
    print(f"La persona pertenece a la categoria{categoria}")