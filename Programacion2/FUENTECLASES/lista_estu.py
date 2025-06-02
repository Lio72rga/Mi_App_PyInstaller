# Lista de estudiantes (cada estudiante es un diccionario)
estudiantes = [
    {"nombre": "Ana", "edad": 20, "materias": ["Matemática", "Programación", "Inglés Técnico"]},
    {"nombre": "Luis", "edad": 22, "materias": ["Estadística", "Bases de Datos", "Inglés Técnico"]},
    {"nombre": "María", "edad": 19, "materias": ["Lógica", "Probabilidad", "Programación"]}
]

# Función para mostrar todos los estudiantes
def mostrar_estudiantes():
    for estudiante in estudiantes:
        print(f"\nNombre: {estudiante['nombre']}")
        print(f"Edad: {estudiante['edad']}")
        print("Materias:")
        for materia in estudiante['materias']:
            print(f" - {materia}")

# Función para buscar un estudiante por nombre
def buscar_estudiante(nombre):
    for estudiante in estudiantes:
        if estudiante["nombre"].lower() == nombre.lower():
            return estudiante
    return None

# Función para agregar una materia a un estudiante
def agregar_materia(nombre, nueva_materia):
    estudiante = buscar_estudiante(nombre)
    if estudiante:
        if nueva_materia not in estudiante["materias"]:
            estudiante["materias"].append(nueva_materia)
            print(f"Materia '{nueva_materia}' agregada a {nombre}.")
        else:
            print(f"{nombre} ya está cursando '{nueva_materia}'.")
    else:
        print(f"No se encontró un estudiante con el nombre '{nombre}'.")

# Función para quitar una materia
def quitar_materia(nombre, materia):
    estudiante = buscar_estudiante(nombre)
    if estudiante:
        if materia in estudiante["materias"]:
            estudiante["materias"].remove(materia)
            print(f"Materia '{materia}' quitada de {nombre}.")
        else:
            print(f"{nombre} no cursa la materia '{materia}'.")
    else:
        print(f"No se encontró un estudiante con el nombre '{nombre}'.")


# === Pruebas de las funciones ===
print("=== Lista de estudiantes ===")
mostrar_estudiantes()

print("\n=== Buscar estudiante ===")
nombre_buscado = "Luis"
resultado = buscar_estudiante(nombre_buscado)
if resultado:
    print(f"{nombre_buscado} encontrado: {resultado}")
else:
    print(f"{nombre_buscado} no se encuentra.")

print("\n=== Agregar materia ===")
agregar_materia("Ana", "Física")

print("\n=== Quitar materia ===")
quitar_materia("María", "Programación")

print("\n=== Lista actualizada ===")
mostrar_estudiantes()
