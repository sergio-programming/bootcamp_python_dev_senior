class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad = edad
        self.__cuentaBancaria = 123456
    
    def mostrarInformacion(self):
        return f"Nombre: {self.nombre} // Edad: {self._edad}"
    
    def mostrarCuenta(self):
        return f"Cuenta Bancaria: {self.__cuentaBancaria}"
    
    def mostrarInformacionCompleta(self):
        return self.mostrarCuenta()
    
    
persona1 = Persona("Sergio Pedraza", 36)

#Imprimir los atributos
print(f"Nombre: {persona1.nombre}")
print(f"Edad: {persona1._edad}")

print(f"Estos son los datos: {persona1.mostrarInformacion()}")
print(f"Cuenta Bancaria: #{persona1.mostrarInformacionCompleta()}")