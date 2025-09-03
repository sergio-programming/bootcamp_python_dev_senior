class CalcularImpuesto:
    
    def ejecutar(self, monto):
        return monto * 0.19
    
class AplicarDescuento:
    
    def ejecutar(self, monto, descuento):
        return monto * (descuento/100)

class GenerarFactura:
     
     def ejecutar(self, monto):
         return f"El total de la Factura es: ${monto:.2f}"

class Facturacion:
    def __init__(self):
        self._pasos = []
        
    def agregar_paso(self, paso):
        self._pasos.append(paso)
        
    def procesarFactura(self, monto, descuento):
        print("\nProcesando Factura...")
        for paso in self._pasos:
            if isinstance(paso, CalcularImpuesto):
                impuesto = paso.ejecutar(monto)
                print(f"Impuesto Calculado: ${impuesto} pesos")
                monto += impuesto
            if isinstance(paso, AplicarDescuento):
                descuento = paso.ejecutar(monto, descuento)
                print(f"Descuento Calculado: ${descuento} pesos")
                monto -= descuento
            if isinstance(paso, GenerarFactura):
                print(paso.ejecutar(monto))
                
                
                
facturacion1 = Facturacion()

paso1 = CalcularImpuesto()
paso2 = AplicarDescuento()
paso3 = GenerarFactura()

facturacion1.agregar_paso(paso1)
facturacion1.agregar_paso(paso2)
facturacion1.agregar_paso(paso3)

facturacion1.procesarFactura(756000, 15)
                
            
    
    