# Tupla con 3 estudiantes: (nombre, edad, [materias])
estudiantes = (
    ("Ana", 20, ["Matemática", "Programación", "Inglés Técnico"]),
    ("Luis", 22, ["Estadística", "Bases de Datos", "Inglés Técnico"]),
    ("María", 19, ["Lógica", "Probabilidad", "Programación"])
)

# Mostrar los datos de los estudiantes
for estudiante in estudiantes:
    nombre, edad, materias = estudiante
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print("Materias:")
    for materia in materias:
        print(f" - {materia}")
    print()
