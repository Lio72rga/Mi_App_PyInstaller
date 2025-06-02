class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio:.2f}")
        print(f"Stock disponible: {self.stock} unidades")

    def actualizar_stock(self, cantidad):
        self.stock += cantidad
        print(f"El stock se ha actualizado. Nuevo stock: {self.stock} unidades")

# Ejemplo de uso
producto1 = Producto("Camiseta", 1200.50, 50)
producto1.mostrar_info()

producto1.actualizar_stock(10)  # Sumar 10 al stock
producto1.actualizar_stock(-5)  # Restar 5 al stock
producto1.mostrar_info()
