# Tupla inicial
tupla_estudiantes = (
    ("Ana", 20, ["Matemática", "Programación", "Inglés"]),
    ("Luis", 22, ["Estadística", "Bases de Datos", "Inglés Técnico"]),
    ("María", 19, ["Lógica", "Probabilidad", "Programación"])
)

# Convertir la tupla en lista
lista_estudiantes = list(tupla_estudiantes)

# Agregar nuevo estudiante
nuevo_estudiante = ("Carlos", 21, ["Álgebra", "Física", "Inglés"])
lista_estudiantes.append(nuevo_estudiante)

# Transformar en diccionario
diccionario_estudiantes = {}
for nombre, edad, materias in lista_estudiantes:
    diccionario_estudiantes[nombre] = {
        "edad": edad,
        "materias": materias
    }

# Imprimir los datos
print("=== DATOS DE LOS ESTUDIANTES ===")
for nombre, datos in diccionario_estudiantes.items():
    print(f"\nNombre: {nombre}")
    print(f"Edad: {datos['edad']}")
    print("Materias:")
    for materia in datos["materias"]:
        print(f" - {materia}")


