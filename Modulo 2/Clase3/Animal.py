class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def comunicar(self):
        pass
    

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza
        
    def comunicar(self):
        return f"{self.nombre} esta ladrando"
    
class Gato(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza
        
    def comunicar(self):
        return f"{self.nombre} esta mauyando"
  
  
perro1 = Perro("Dogo", "Gran Danes")   
perro2 = Perro("Kaiser", "Labrador")
gato1 = Gato("Michi", "Siames")   
gato2 = Gato("Bills", "Maine Coon")   
    
animales = [perro1, perro2, gato1, gato2]

for animal in animales:
    print(animal.comunicar())