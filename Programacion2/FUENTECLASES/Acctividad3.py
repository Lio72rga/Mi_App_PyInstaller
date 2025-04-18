# Paso 1: Crear un diccionario que contenga nombre, edad y carrera de un 
#alumno y mostrar el diccionario completo.
alumno = {"nombre": "Daniel", "edad": 21, "carrera": "Analista de Sistemas"}
print("Diccionario completo:", alumno)

# Paso 2: Usar el método get para mostrar el valor de la clave "nombre"
print("Nombre del alumno:", alumno.get("nombre"))

# Paso 3: Cambiar la edad del alumno y mostrar el diccionario completo
alumno["edad"] = 24
print("Diccionario actualizado:", alumno)

# Paso 4: Agregar un par clave-valor para el sexo del alumno y mostrarlo
alumno["sexo"] = "Masculino"
print("Diccionario con sexo agregado:", alumno)
# Paso 5: Usar el método pop() para remover la edad del alumno y mostrarlo
alumno.pop("edad")
print("Diccionario sin edad:", alumno)

# Paso 6: Crear un diccionario de notas de un alumno
notas = {
    "Programación II": 8,
    "Ciencia de Datos": 9,
    "Programación I": 7
}

# Paso 7: Mostrar todos los ítems del diccionario de notas
print("Notas del alumno:", notas.items())
# Paso 8: Crear una copia del diccionario de notas y mostrarlo
copia_notas = notas.copy()
print("Copia del diccionario de notas:", copia_notas)