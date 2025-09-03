# Uso de breakpoints simples
from textwrap import dedent

class Empleado:
    def __init__(self, nombre, ventas):
        self.nombre = nombre
        self.ventas = ventas
        
    def calculoComision(self):
        if self.ventas > 5000:
            print(f"\nEmpleado: {self.nombre} // Ventas: {self.ventas} // Comision del 10%")
            return self.ventas * 0.1
        print(f"\n Empleado: {self.nombre} // Ventas: {self.ventas} // Comision del 5%")
        return self.ventas * 0.05
    
empleados = [
    Empleado("Ana", 6000),
    Empleado("Luis", 4500),
    Empleado("Checho", 6500),
    Empleado("Luisa", 4800)
]

for emp in empleados:
    print(dedent(f"""
                 Empleado: {emp.nombre}
                 Ventas: ${emp.ventas} USD
                 Comision: ${emp.calculoComision()} USD"""))