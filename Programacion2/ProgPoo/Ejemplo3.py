from Programacion2.ProgPoo.Ejemplo1 import Persona
class Empeado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad) #Llamando al constructor de la clase base
        self.salario = salario #Atributo de instancia

    def mostrar_info(self):
        print(f"{self.nombre}, {self.edad}, años, gana ${self.salario}")
empl = Empeado("Carlos", 40, 120000)
empl.saludar() # Heredado de la clase Persona
empl.mostrar_info() # Propio de la clase Empleado

