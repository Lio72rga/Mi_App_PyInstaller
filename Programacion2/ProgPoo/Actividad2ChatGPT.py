# Clase principal (padre)
class RecursoDigital:
	def __init__(self, titulo, autor, año):
		self.titulo = titulo
		self.autor = autor
		self.año = año

	def mostrar_info(self):
		return f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.año}"

# Clase que hereda de RecursoDigital
class LibroDigital(RecursoDigital):
	def __init__(self, titulo, autor, año, formato, tamaño_mb):
		super().__init__(titulo, autor, año)
		self.formato = formato
		self.tamaño_mb = tamaño_mb

	def mostrar_info(self):
		info_base = super().mostrar_info()
		return f"{info_base}, Formato: {self.formato}, Tamaño: {self.tamaño_mb} MB"

# Crear instancia de LibroDigital
libro = LibroDigital("1984", "George Orwell", 1949, "PDF", 1.2)
print(libro.mostrar_info())
