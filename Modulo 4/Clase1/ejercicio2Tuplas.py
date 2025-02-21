from typing import Tuple

def obtenerDatosEmpleado(empleado: Tuple[int, str, str]) -> Tuple:
    idEmpleado, nombreEmpleado, cargoEmpleado = empleado
    print(f"Id: {idEmpleado} // Nombre: {nombreEmpleado} // Cargo: {cargoEmpleado}")
    
def analizarSalarios(salarios: Tuple[int, ...]) -> None:
    print(f"Salarios tabulados: {salarios}")
    print(f"Cantidad de salarios registrados: {len(salarios)}")
    print(f"El salario mas alto registrado es: ${max(salarios)}")
    print(f"El salario mas bajo registrado es: ${min(salarios)}")
    print(f"La suma de los salarios registrados es: ${sum(salarios)}")
    print(f"Los salarios registrados de forma ordenada: {sorted(salarios)}")
    
    salarioBuscado = 2300000
    print(f"El salario que tiene un valor de ${salarioBuscado} se encuentra registrado {salarios.count(salarioBuscado)} veces")
    
    if salarioBuscado in salarios:
        print(f"El salario que tiene un valor de ${salarioBuscado} se encuentra en la posición {salarios.index(salarioBuscado)}")
        
def main():
    empleado = (1010, "Sergio Pedraza", "Programador Senior")
    
    obtenerDatosEmpleado(empleado)
    
    salariosEmpleados = (2300000, 2850000, 1915000, 3400000, 3650000, 2300000, 4560000, 3880000)
    
    analizarSalarios(salariosEmpleados)
    
if __name__ == "__main__":
    main()