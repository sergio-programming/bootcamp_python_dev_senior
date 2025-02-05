from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Vendedor(ABC):
    nombre: str
    ventas: float
    
    @abstractmethod
    def calcularComision(self) -> float:
        pass

@dataclass
class VendedorJunior(Vendedor):
    
    def calcularComision(self) -> float:
        return self.ventas * 0.10
    
@dataclass
class VendedorSenior(Vendedor):
    
    def calcularComision(self) -> float:
        return self.ventas * 0.20
