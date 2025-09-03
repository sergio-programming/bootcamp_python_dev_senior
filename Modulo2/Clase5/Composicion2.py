class Tarea:
    def __init__(self):
        pass
    
    def ejecutar(self):
        pass
    
class ProcesarOrden(Tarea):
    def __init__(self):
        pass
    
    def ejecutar(self):
        return "Procesando ordenes de compra"
    
class LiquidarInstruccion(Tarea):
    def __init__(self):
        pass
    
    def ejecutar(self):
        return "Liquidando una instrucción"
    
class RegistrarFactura(Tarea):
    def __init__(self):
        pass
    
    def ejecutar(self):
        return "Registrando una factura"
    
class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas = []
        
        
    def asignarTarea(self, tarea):
        self.tareas.append(tarea)
        
    def realizarTarea(self):
        print(f"El empleado {self.nombre} esta ejecutando las siguientes tareas:")
        for i, tarea in enumerate (self.tareas, start=1):
            print(f"Tarea {i}: {tarea.ejecutar()}")
            
            
empleado1 = Empleado("Sergio Pedraza")
tarea1 = RegistrarFactura()
tarea2 = ProcesarOrden()
tarea3 = LiquidarInstruccion()

empleado1.asignarTarea(tarea1)
empleado1.asignarTarea(tarea2)
empleado1.asignarTarea(tarea3)

empleado1.realizarTarea()