class Inventario:
    def __init__(self):
        self.cantidad_inicial = 0
        self.cantidad_vendida = 0
        self.inventario_actual = 0

    def ingresar_cantidad_inicial(self, cantidad):
        self.cantidad_inicial = cantidad
        self.inventario_actual = cantidad

    def ingresar_cantidad_vendida(self, cantidad):
        self.cantidad_vendida = cantidad

    def actualizar_inventario(self):
        if self.cantidad_vendida > self.cantidad_inicial:
            return "Alerta: Venta Excedida"
        self.inventario_actual = self.cantidad_inicial - self.cantidad_vendida
        if self.inventario_actual < 10:
            return "Alerta: Inventario Bajo"
        return f"Inventario actualizado: {self.inventario_actual}"

# Ejemplo de uso
tienda = Inventario()
tienda.ingresar_cantidad_inicial(20)
print(tienda.actualizar_inventario())  # Sin ventas aún, debe mostrar 20
print(tienda.ingresar_cantidad_vendida(5))
print(tienda.actualizar_inventario())  # Después de vender 5, debe mostrar 15
print(tienda.ingresar_cantidad_vendida(12))
print(tienda.actualizar_inventario())  # Después de vender 12, debe mostrar "Alerta: Inventario Bajo"
print(tienda.ingresar_cantidad_vendida(25))
print(tienda.actualizar_inventario())  # Intentar vender más de lo disponible, debe mostrar "Alerta: Venta Excedida"
