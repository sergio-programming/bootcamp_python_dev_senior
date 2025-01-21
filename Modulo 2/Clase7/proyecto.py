from abc import ABC, abstractmethod
from datetime import datetime

class Persona(ABC):
    def __init__(self, nombre, telefono, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
    
    @abstractmethod    
    def mostrarInformacion(self):
        pass
    
    
class Mascota(ABC):
    def __init__(self, nombre, especie, raza, edad):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.historialCitas = []
        
    @abstractmethod
    def agregarAlHistorial(self, detallesServicio):
        pass
    
class Cita(ABC):
    def __init__(self, fecha, hora, servicio, veterinario):
        self.fecha = fecha
        self.hora = hora
        self.servicio = servicio
        self.veterinario = veterinario
    
    @abstractmethod()    
    def actualizar(self, **kwargs):
        pass
    
#Definicion de las subclases
class Cliente(Persona):
    def __init__(self, nombre, telefono, direccion):
        super().__init__(nombre, telefono, direccion)
        self.mascotas = []
        
    def agregarMascota(self, mascota):
        self.mascotas.append(mascota)
        
    def mostrarInformacion(self):
        return f"Cliente: {self.nombre}, Telefono: {self.telefono}, Direccion: {self.direccion}"
    
    
class RegistroMascota(Mascota):
    def agregarAlHistorial(self, detallesServicio):
        self.historialCitas.append(detallesServicio)
        
    def obtenerHistorial(self):
        return self.historialCitas
    
class CitaMascota(Cita):
    def actualizar(self, **kwargs):
        for clave, valor in kwargs.items():
            if hasattr(self, clave):
                setattr(self, clave, valor)
                
class SistemaVeterinaria:
    def __init__(self):
        self.clientes = []
        
    def registrarCliente(self):
        try:
            nombre = input("Ingrese el nombre del cliente: ").strip()
            telefono = input("Ingrese el número de telefono del cliente: ").strip()
            direccion = input("Ingrese la dirección del cliente: ").strip()
            
            if nombre is None or telefono is None or direccion  is None:
                raise ValueError("Todos los campos son obligatorios. Por favor diligenciar nuevamente.")  
            
            cliente = Cliente(nombre, telefono, direccion)
            self.clientes.append(cliente)
            print("Cliente registrado con exito!!!")
              
        except ValueError as e:
            print(f"Error: {e}")
        
    def registrarMascota(self):
        try:
            nombreCliente = input("Ingrese el nombre del cliente que es dueño de la mascota: ").strip()
            cliente = next((c for c in self.clientes if c.nombre == nombreCliente), None)
            
            if not cliente:
                raise ValueError("Cliente no registrado.")
            
            
            nombre = input("Ingrese el nombre de la mascota: ").strip()
            especie = input("Ingrese la especie de la mascota: ").strip()
            raza = input("Ingrese la raza de la mascota: ").strip()
            try:
                edad = int(input("Ingrese la edad de la mascota: "))
            except ValueError:
                print("Debe ingresar un valor númerico para la edad de la mascota. Intente nuevamente.")
         
            if nombre is None or especie is None or raza is None or edad is None:
                raise ValueError("Todos los campos son obligatorios. Por favor diligenciar nuevamente.")
            
            
        except ValueError as e:
            print(f"Error: {e}")
        
        