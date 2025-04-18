"""Ordenación basada en atributos de objetos
Si tienes una lista de objetos y quieres ordenarla en 
función de un atributo específico de esos objetos, puedes usar el
argumento key con una función que extraiga ese atributo."""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
people =[Person("Alice", 25), Person("Bob", 30), Person("Eve", 22), Person("David",28)]
sorted_people = sorted(people, key=lambda person: person.age)
for person in sorted_people:
    print(person.name, person.age)