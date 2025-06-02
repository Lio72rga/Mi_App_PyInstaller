#CLASES
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre #Atributo de instancia
        self.edad = edad #Atributo de instancia

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad} años")
        
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")
Persona1 = Persona("Ana", 30)
Persona2 = Persona("Luis", 25)
Persona1.saludar() #Hola, soy Ana y tengo 30 años
Persona2.saludar() #Hola, soy Luis y tengo 25 años
print(Persona1.nombre) #Ana
Persona1.edad = 31 #Modificando el atributo edad de Persona1
print(Persona1.edad) #31
Persona1.mostrar() #Nombre: Ana, Edad: 31 años
#Ejemplo de herencia
def cumplir_anios(self):
    self.edad += 1
    print(f"Feliz cumpleaños, {self.nombre}! ahora tienes {self.edad} años")

# Adding the new method to the existing Persona class
Persona.cumplir_anios = cumplir_anios
Persona1.cumplir_anios() #Feliz cumpleaños, Ana
Persona1.mostrar() #Nombre: Ana, Edad: 32 años.
