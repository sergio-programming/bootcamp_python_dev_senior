import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.DEBUG)

@dataclass
class Vendedor:
    nombre: str
    ventasTotales: float
    
    def calculoComision(self) -> str:
        if self.ventasTotales > 10000:
            comision = self.ventasTotales * 0.2
            logging.debug(f"{self.nombre} ha alcanzado el umbral de ventas. La comision calculada es de ${comision} USD")
        else:
            comision = self.ventasTotales * 0.1
            logging.debug(f"{self.nombre} no ha alcanzado el umbral de ventas. La comision calculada es de ${comision} USD")
        return f"{self.nombre} su comision es de ${comision} USD"
    
if __name__ == "__main__":
    vendedor1 = Vendedor("Sergio", 15000)
    vendedor2 = Vendedor("Valentina", 9500)
    
    print(vendedor1.calculoComision())    
    print(vendedor2.calculoComision())    
        
            