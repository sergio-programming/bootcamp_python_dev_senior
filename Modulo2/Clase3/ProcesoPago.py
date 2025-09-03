#Interfaces
from abc import ABC, abstractmethod

class ProcesoPago(ABC):
    
    @abstractmethod
    def procesoPago(self, cantidad: float) -> None:
        pass
    
    @abstractmethod    
    def reembolsoPago(self, transaccionId: str) -> None:
        pass
    

class Paypal(ProcesoPago):
    
    def procesoPago(self, cantidad: float) -> None:
        print(f"Procesando pago con Paypal de ${cantidad} dolares")
        
    def reembolsoPago(self, transaccionId: str) -> None:
        print(f"Reembolsando Id Transacción #{transaccionId}")
        
        
class Stripe(ProcesoPago):
    
    def procesoPago(self, cantidad: float) -> None:
        print(f"Procesando pago con Stripe de ${cantidad} dolares")
        
    def reembolsoPago(self, transaccionId: str) -> None:
        print(f"Reembolsando Id Transacción #{transaccionId}")
        

if __name__ == "__main__":
    procesoPaypal = Paypal()
    procesoStripe = Stripe()
    
    procesoPaypal.procesoPago(540)
    procesoPaypal.reembolsoPago("FCA345#004")
    
    procesoStripe.procesoPago(925)
    procesoStripe.reembolsoPago("FCA345#016")