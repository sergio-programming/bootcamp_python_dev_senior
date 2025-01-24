import logging
from dataclasses import dataclass

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='ejercicio2.log',
    filemode='w'
)

#Crear un nuevo handler para gestionar mensaje de auditoria .log y por consola
console_handler = logging.StreamHandler() # Crear una instancia, un nuevo manejador
console_handler.setLevel(logging.DEBUG) # COnfigurar el nivel del logging, en este caso el nivel mas leve
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',)) # Dando formato de salida al logging
logging.getLogger().addHandler(console_handler) # Agregando la instancia console_handler al manejador principal

@dataclass
class Factura:
    cliente: str
    cantidad: int
    precioUnitario: float
    
    def procesar(self):
        try:
            logging.info(f"Iniciando el proceso de facturacion para el cliente {self.cliente}")
            
            if self.cantidad <= 0:
                raise ValueError("La cantidad del producto debe ser mayor a cero")
            if self.precioUnitario <= 0:
                raise ValueError("EL precio debe ser mayo a cero")
            
            total = self.cantidad * self.precioUnitario
            logging.info(f"Factura procesada con exito. Total Compra: ${total} - Cliente: {self.cliente}") 
            
        except ValueError as e:
            logging.error(f"Error de validación del cliente {self.cliente}: {e}")
        except Exception as e:
            logging.critical(f"Error inesperado al momento de procesar la factura del cliente {self.cliente}: {e}")
        finally:
            logging.info(f"El proceso de facturacion para el cliente {self.cliente} finalizo")
            
if __name__ == "__main__":
    factura1 = Factura("Sergio", 15, 56000)
    factura1.procesar()