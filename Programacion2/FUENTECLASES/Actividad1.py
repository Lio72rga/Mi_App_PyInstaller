# Actividad 1. 
# 1. Crear una lista con nombres de provincias argentinas (más de 5 elementos) e imprimirla
provincias_argentinas = ["Buenos Aires", "Córdoba", "Santa Fe", "Mendoza", "Tucumán", "Entre Ríos", "Salta"]
print("Lista de provincias argentinas:")
print(provincias_argentinas)

# 2. Imprimir el tercer elemento de la lista (índice 2)
print("Tercer elemento de la lista:")
print(provincias_argentinas[2])

# 3. Imprimir del segundo al cuarto elemento de la lista (índices 1 a 3, porque el último no se incluye)
print("Segundo al cuarto elemento:")
print(provincias_argentinas[1:4])

# 4. Mostrar el tipo de dato de la lista
print("Tipo de dato de la lista:")
print(type(provincias_argentinas))

# 5. Mostrar los primeros 4 elementos de la lista
print("Primeros cuatro elementos de la lista:")
print(provincias_argentinas[:4])

# 6. Agregar una provincia más (una que ya exista y otra que no)
provincias_argentinas.append("Buenos Aires")  # Provincia que ya existe
provincias_argentinas.append("Neuquen")        # Nueva provincia
print("Lista después de agregar dos provincias:")
print(provincias_argentinas)

# 7. Agregar una provincia en la cuarta posición
provincias_argentinas.insert(3, "La Rioja")
print("Lista después de agregar 'La Rioja' en la cuarta posición:")
print(provincias_argentinas)
# 8. Extender otra lista a la ya creada
provincias_extra = ["Misiones", "San Juan", "Corrientes"]
provincias_argentinas.extend(provincias_extra)
print("Lista después de extender con otra lista:")
print(provincias_argentinas)

# 9. Eliminar un elemento de la lista
provincias_argentinas.remove("Buenos Aires")  # Aquí eliminamos "Buenos Aires"
print("Lista después de eliminar 'Buenos Aires':")
print(provincias_argentinas)

# 10. Extraer el último elemento de la lista, guardarlo en una variable e imprimirlo
ultima_provincia = provincias_argentinas.pop()  # `pop()` extrae y elimina el último elemento
print("Última provincia extraída:")
print(ultima_provincia)
print("Lista después de extraer el último elemento:")
print(provincias_argentinas)