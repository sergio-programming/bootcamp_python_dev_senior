import pdb
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Empleado(ABC):
    nombre: str
    salarioBase: float
    
    @abstractmethod
    def calcularSalario(self):
        pass

@dataclass  
class Manager(Empleado):
    def calcularSalario(self):
        return self.salarioBase + 5000

@dataclass
class Developer(Empleado):
    def calcularSalario(self):
        return self.salarioBase + 2000
    
def calcularTotalSalario(empleado: Empleado) -> str:
    """
    Calcula el salario total de un empleado.

    Args:
        empleado (Empleado): El empleado cuyo salario se calculará.

    Returns:
        str: Un mensaje con el nombre del empleado y su salario total.
    """
    # Activación del debugger:
    # n: Avanza línea por línea.
    # s: Salta de función en función.
    # c: Continua hasta la siguiente pausa.
    # p variable: Muestra el valor de una variable.
    pdb.set_trace()
    return f"{empleado.nombre} su salario es de {empleado.calcularSalario()}"

if __name__ == "__main__":
    manager = Manager("Johan", 30000)
    developer = Developer("Sergio", 25000)
    
    print(calcularTotalSalario(manager))
    print(calcularTotalSalario(developer))