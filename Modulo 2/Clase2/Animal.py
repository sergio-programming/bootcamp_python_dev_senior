class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hablar(self):
        return "Todo animal habla de alguna forma"
    
    def __str__(self):
        return f"EL nombre del animal es {self.nombre}"
    
class Perro(Animal):
    def __init__(self, nombre, raza, edad):
        super().__init__(nombre)
        self.raza = raza
        self.edad = edad
    
    def ladrar(self):
        return f"{self.nombre} esta ladrando"
    
    def __str__(self):
        return f"""Nombre: {self.nombre}
Raza: {self.raza}
Edad: {self.edad} años"""
    
animal1 = Animal("Dolly")

print(animal1.hablar())
print(animal1.__str__())
print()

perro1 = Perro("Dogo", "Bull Terrier", 4)
print(perro1.ladrar())
print(perro1.__str__())

