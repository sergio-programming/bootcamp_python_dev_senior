from abc import ABC, abstractmethod

class EstrategiaTarifa(ABC):
    
    @abstractmethod
    def calcularTarifa(self, distancia, tiempo):
        raise NotImplementedError("Se debe implementar este metodo")
    
    
class TarifaFija(EstrategiaTarifa):
    def calcularTarifa(self, distancia, tiempo):
        return 300
    
class TarifaHora(EstrategiaTarifa):
    def calcularTarifa(self, distancia, tiempo):
        return tiempo * 25
    
class TarifaKilometro(EstrategiaTarifa):
    def calcularTarifa(self, distancia, tiempo):
        return distancia * 2
    
class CalculadoraTarifa:
    def __init__(self, estrategia):
        self.estrategia = estrategia
        
    def cambiarEstrategia(self, estrategia):
        self.estrategia = estrategia
        
    def calcular(self, distancia, tiempo):
        return self.estrategia.calcularTarifa(distancia, tiempo)
    
arriendo1 = TarifaFija()
calculadora = CalculadoraTarifa(arriendo1)
print(f"La tarifa fija es: ${calculadora.calcular(10, 5)}")

calculadora.cambiarEstrategia(TarifaHora())
print(f"La tarifa por hora es: ${calculadora.calcular(100, 2)}")