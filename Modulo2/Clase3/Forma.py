from abc import ABC, abstractmethod
import math

class Forma(ABC):
    
    @abstractmethod
    def __init__(self):
        pass
        
    @abstractmethod
    def perimetro(self):
        pass
        
    @abstractmethod
    def area(self):
        pass
    
class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
        
    def perimetro(self):
        perimetro = 2 * math.pi * self.radio
        return f"El perimetro del circulo es: {perimetro:.2f} m"
        
    def area(self):
        area = math.pi * math.pow(self.radio,2)
        return f"El areá del circulo es: {area:.2f} m²"
    
class Rectangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def perimetro(self):
        perimetro = 2 * (self.base + self.altura)
        return f"El perimetro del rectangulo es: {perimetro} m"
        
    def area(self):
        area = self.base * self.altura
        return f"El areá del rectangulo es: {area} m²"
    
class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
        
    def perimetro(self):
        perimetro = self.lado * 4
        return f"El perimetro del cuadrado es: {perimetro} m"
        
    def area(self):
        area = math.pow(self.lado, 2)
        return f"El areá del cuadrado es: {area} m²"
    

circulo1 = Circulo(5)
circulo2 = Circulo(8)
rectangulo1 = Rectangulo(12, 6)
rectangulo2 = Rectangulo(15, 9)
cuadrado1 = Cuadrado(7)
cuadrado2 = Cuadrado(10)

formas = [circulo1, circulo2, rectangulo1, rectangulo2, cuadrado1, cuadrado2]

for forma in formas:
    print(forma.perimetro())
    print(forma.area())
    print()