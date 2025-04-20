class Animal:
    def hablar(self):
        print("El animal hace un sonido")
class Perro(Animal):
    def hablar(self):
        print("Guau!")
class Gato(Animal):   
    def hablar(self):
        print("Miau!")
def hacer_hablar(animal):
    animal.hablar()
hacer_hablar(Perro()) #Guau! 
hacer_hablar(Gato()) #Miau!
#Ejemplo de polimorfismo
#El polimorfismo es la capacidad de un objeto de tomar muchas formas. En este caso, 
# el método "hablar" se comporta de manera diferente según el tipo de objeto que lo invoque.   