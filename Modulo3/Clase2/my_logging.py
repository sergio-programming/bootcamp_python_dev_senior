import logging
from dataclasses import dataclass, field

"""
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
    )

logging.DEBUG("Este es el mensaje del DEBUG")
logging.INFO("Este es el mensaje del INFO")
logging.warning("Este es el mensaje del warning")
logging.error("Este es el mensaje del error")
logging.critical("Este es el mensaje critico")
"""

"""
App que permite llevar seguimiento de compras/fallos en este tipo de transacción.
Esta App registrara la cantidad de productos comprados
"""

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='registro.log',
    filemode='a'
)

@dataclass
class Producto:
    nombre: str
    precio: float
    cantidad: int
    
    def comprar(self, cantidad: int):
        if cantidad > self.cantidad:
            logging.error(f"Error: No hay suficiente cantidad de producto {self.nombre}. Disponibilidad: {self.cantidad} UND")
            raise ValueError(f"Error: No hay suficiente cantidad de producto {self.nombre}. Disponibilidad: {self.cantidad} UND")
        
        else:
            self.cantidad -= cantidad
            logging.info(f"La compra fue exitosa. Cantidad disponible: {self.cantidad} UND")
            return self.precio * cantidad
        
@dataclass
class Tienda:
    productos: list[Producto] = field(default_factory=list)
    
    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)
        logging.debug(f"El producto {producto.nombre} fue agregado con exito. // Precio: ${producto.precio} pesos // Cantidad: {producto.cantidad} UND")
        
    def realizar_compra(self, nombre_producto: str, cantidad: int):
        producto = next((p for p in self.productos if p.nombre == nombre_producto), None)
        
        if producto is None:
            logging.warning(f"Producto {nombre_producto} no encontrado en la tienda.")
            print(f"Producto {nombre_producto} no encontrado en la tienda.")
            return

        try:
            total = producto.comprar(cantidad)
            logging.info(f"""Compra realizada:
                    Producto: {nombre_producto}
                    Cantidad: {cantidad}
                    Total: ${total} pesos
                """)
            return total
        except ValueError as e:
            logging.error(f"Error al efectuar la compra: {e}")
            print(f"Error al efectuar la compra: {e}")
                
if __name__ == "__main__":
    tienda = Tienda()
    inventario_portatil = Producto()
    tienda.agregar_producto(inventario_portatil)
    tienda.realizar_compra("Portatil", 4)
    
    inventario_teclado = Producto(nombre = "Teclado", precio=50, cantidad=5)
    tienda.agregar_producto(inventario_teclado)
    tienda.realizar_compra("Teclado", 10)