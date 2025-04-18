#Calculadora de descuento: Solicita al usuario ingresar el precio original de
#un producto. Luego, calcula y muestra el precio final después del
#descuento. Tener en cuenta que si se ingresa un precio de producto mayor
#o igual a $12.999 entonces se realizará el descuento del 30%, de lo
#contrario, se realizará el 20%.

#Definimos precio producto
precio_producto = float(input("Ingrese el precio de un producto: $"))

#calcular el descuento

if precio_producto >= 12.999:
    descuento = precio_producto * 0.3 

else:
    descuento = precio_producto * 0.2

#calcular precio final

precio_final = precio_producto - descuento

#mostrar el precio final y el descuento

print(f"Precio original :${precio_producto: .3f}")
print (f"descuento :${descuento: .3f}")
print (f"Precio final :${precio_final: .3f}")