def busqueda_hash(tabla_hash, clave):
    if clave in tabla_hash:
        return tabla_hash[clave]
    else:
        return None
#Ejemplo de uso
tabla ={
    "Juan": 25,
    "Maria": 30,
    "Pedro": 28,
    "Ana": 35
}
calve_busqueda = "Pedro"
resultado = busqueda_hash(tabla, calve_busqueda)
print(resultado) #Salida 28