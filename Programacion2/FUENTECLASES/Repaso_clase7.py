#Clase vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}")
        
#SubClase auto hereda de vehiculo
class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)
        self.puertas = puertas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Puertas: {self.puertas}")
        
#SobreEscritura de la funcion mostrar_info
def mostrar_info(self):
    super().mostrar_info()
    print(f"Puertas: {self.puertas}")

#Crear intancia de la clase Vehiculo
mi_auto = Auto("Toyota", "Corolla", 2020, 4)
mi_auto.mostrar_info()

print("===================================")