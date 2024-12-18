from abc import ABC, abstractmethod

class EstrategiaDescuento(ABC):
    
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def calcular(self, monto):
        pass
    
class sinDescuento(EstrategiaDescuento):
    
    def __init__(self):
        pass
    
    def calcular(self, monto):
        return monto
    
class DescuentoPorcentaje(EstrategiaDescuento):
    
    def __init__(self, porcentaje):
        self.porcentaje = porcentaje
        
    def calcular(self, monto):
        return monto - (monto * self.porcentaje / 100)
    
class DescuentoFijo(EstrategiaDescuento):
    
    def __init__(self, montoDescuento):
        self.montoDescuento = montoDescuento
        
    def calcular(self, monto):
        return monto - self.montoDescuento
    
class Pedido:
    
    def __init__(self, monto, estrategiaDescuento: EstrategiaDescuento):
        self.monto = monto
        self.estrategiaDescuento = estrategiaDescuento
        
    def calcularTotal(self):
        return self.estrategiaDescuento.calcular(self.monto)
    
pedido1 = Pedido(250000, sinDescuento())
print(f"Total sin descuento: ${pedido1.calcularTotal()}")

pedido2 = Pedido(855000, DescuentoPorcentaje(15))
print(f"Total con %15 de descuento: ${pedido2.calcularTotal()}")

pedido3 = Pedido(920000, DescuentoFijo(85000))
print(f"Total con descuento fijo de $85.000: ${pedido3.calcularTotal()}")