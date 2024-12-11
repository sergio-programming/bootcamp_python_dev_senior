import threading
from abc import ABC, abstractmethod

#Patron Singleton
class SistemaFacturacion:
    
    _instancia = None
    _lock = threading.Lock()
    
    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super(SistemaFacturacion, cls).__new__(cls)
            cls._instancia._inicializacionHistorico()
        return cls._instancia
        
        
        """
        with cls._lock:
            if cls._instancia is None:
                cls._instancia = super(SistemaFacturacion, cls).__new__(cls)
                cls._instancia._inicializacionHistorico()
            return cls._instancia    
        """    

    def _inicializacionHistorico(self):
        self.historial = []
        print("Sistema de facturación inicializado")
        
    def registrarOperacion(self, operacion):
        self.historial.append(operacion)
        print(f"La operacion fue registrada: {operacion}")
        
        
#Clase Abstracta
class ProcesoDeNegocio(ABC):
    
    @abstractmethod
    def ejecutar(self):
        pass
    
class ProcesarPedido(ProcesoDeNegocio):
    
    def ejecutar(self):
        print("Procesando pedido...")
        return "Pedido procesado"
    
class ProcesarFactura(ProcesoDeNegocio):
    
    def ejecutar(self):
        print("Procesando factura...")
        return "Factura procesada"
    
#Patron Factory
class FabricaProcesoDeNegocio:
    
    @staticmethod
    def crearProceso(tipoProceso):
        if tipoProceso == "pedido":
            return ProcesarPedido()
        
        elif tipoProceso == "factura":
            return ProcesarFactura()
        
        else:
            raise Exception(f"El proceso {tipoProceso} no existe")


if __name__ == "__main__":
    
    sistema_Facturacion = SistemaFacturacion()
    
    proceso1 = FabricaProcesoDeNegocio.crearProceso("pedido")
    proceso2 = FabricaProcesoDeNegocio.crearProceso("factura")
    
    resultadoPedido1 = proceso1.ejecutar()
    sistema_Facturacion.registrarOperacion(resultadoPedido1)
    
    resultadoPedido2 = proceso2.ejecutar()
    sistema_Facturacion.registrarOperacion(resultadoPedido2)
    
print("HISTORICO DE PROCESOS DE NEGOCIO")
for operacion in sistema_Facturacion.historial:
    print(f"Transaccion: {operacion}")