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
            
            if not nombre or not telefono or not direccion:
                raise ValueError("Todos los campos son obligatorios. Por favor diligenciar nuevamente.")  
            
            cliente = Cliente(nombre, telefono, direccion)
            self.clientes.append(cliente)
            print("¡Cliente registrado con exitosamente!")
              
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
         
            if not nombre or not especie or not raza or not edad:
                raise ValueError("Todos los campos son obligatorios. Por favor diligenciar nuevamente.")
            
            mascota = RegistroMascota(nombre, especie, raza, edad)
            cliente.agregarMascota(mascota)
            print("¡Mascota registrada exitosamente!")
            
            
        except ValueError as e:
            print(f"Error: {e}")
        
    
    def programarCita(self):
        try:
            nombreCliente = input("Ingrese el nombre del cliente que es dueño de la mascota: ").strip()
            nombreMascota = input("Ingrese el nombre de la mascota: ").strip()
            
            cliente = next((c for c in self.clientes if c.nombre == nombreCliente), None)
            if not cliente:
                raise ValueError("Cliente no registrado")
            
            mascota = next((m for m in self.cliente.mascotas if m.nombre == nombreMascota), None)
            if not mascota:
                raise ValueError("Mascota no registrada")
            
            fecha = input("Por favor ingrese la fecha de la cita (AAAA-MM-DD): ").strip()
            hora = input("Por favor ingrese la hora de la cita (HH:MM): ").strip()
            servicio = input("Por favor ingrese el servicio deseado (Consulta, Vacunación, Cirugia, etc): ").strip()
            veterinario = input("Por favor ingrese el nombre del veterinario: ").strip()
            
            datetime.strptime(fecha, "%Y-%m-%d")
            datetime.strptime(hora, "%H:%M")
            
            if not servicio or not veterinario:
                raise ValueError("Todos los campos son obligatorios. Por favor diligenciar nuevamente.")
            
            cita = CitaMascota(fecha, hora, servicio, veterinario)
            mascota.agregarAlHistorial(cita)
            print("¡Cita agregada exitosamente!")
        
        except ValueError as e:
            print(f"Error: {e}")
            
    def actualizarCita(self):
        try:
            nombreCliente = input("Ingrese el nombre del cliente que es dueño de la mascota: ").strip()
            nombreMascota = input("Ingrese el nombre de la mascota: ").strip()
            
            cliente = next((c for c in self.clientes if c.nombre == nombreCliente), None)
            if not cliente:
                raise ValueError("Cliente no registrado")
            
            mascota = next((m for m in self.cliente.mascotas if m.nombre == nombreMascota), None)
            if not mascota:
                raise ValueError("Mascota no registrada")
            
            if not mascota.historialCitas:
                raise ValueError("La mascota no tiene citas registradas")
            
            print("\nCitas registradas de la mascota:")
            for i, cita in enumerate(mascota.historialCitas, start=1):
                print(f"Cita #{i}:")
                print(f"Fecha: {cita.fecha}")
                print(f"Fecha: {cita.hora}")
                print(f"Fecha: {cita.servicio}")
                print(f"Fecha: {cita.veterinario}")
            
            indice = int(input("Seleccione la cita a actualizar: ").strip())
            
            if indice < 1 or indice > len(mascota.historialCitas):
                raise ValueError("La opcion ingresada esta por fuera del rango.")
            
            cita = mascota.historialCitas[indice-1]
            
            fecha = input("Por favor ingrese la fecha de la cita (AAAA-MM-DD): ").strip()
            if fecha == "":
                fecha = cita.fecha
            else:
                datetime.strptime(fecha, "%Y-%m-%d")
            hora = input("Por favor ingrese la hora de la cita (HH:MM): ").strip()
            if hora == "":
                hora = cita.hora
            else:
                datetime.strptime(hora, "%H:%M")
            servicio = input("Por favor ingrese el servicio deseado (Consulta, Vacunación, Cirugia, etc): ").strip()
            if servicio == "":
                servicio = cita.servicio
            veterinario = input("Por favor ingrese el nombre del veterinario: ").strip()
            if veterinario == "":
                veterinario = cita.veterinario
                
            mascota.historialCitas.pop(indice-1)
            cita = CitaMascota(fecha, hora, servicio, veterinario)
            mascota.historialCitas.insert(indice-1, cita)
            
            print("¡Cita actualizada exitosamente")
            
        except ValueError as e:
            print(f"Error: {e}")
            

    def consultarHistorial(self):
        try:
            nombreCliente = input("Ingrese el nombre del cliente que es dueño de la mascota: ").strip()
            nombreMascota = input("Ingrese el nombre de la mascota: ").strip()
            
            cliente = next((c for c in self.clientes if c.nombre == nombreCliente), None)
            if not cliente:
                raise ValueError("Cliente no registrado")
            
            mascota = next((m for m in self.cliente.mascotas if m.nombre == nombreMascota), None)
            if not mascota:
                raise ValueError("Mascota no registrada")
            
            historial = mascota.obtenerHistorial()
            
            if not historial:
                raise ValueError("La mascota no tiene historial de citas registradas")
            
            for i, cita in enumerate(historial, start=1):
                print(f"Cita #{i}:")
                print(f"Fecha: {cita.fecha}")
                print(f"Fecha: {cita.hora}")
                print(f"Fecha: {cita.servicio}")
                print(f"Fecha: {cita.veterinario}")
            
            
        except ValueError as e:
            print(f"Error: {e}")
            
    
    def iniciar(self):
        while True:
            print("\nSistema de Gestión Veterinaria")
            print("1. Registrar Cliente.")
            print("2. Registrar Mascota.")
            print("3. Programar Cita.")
            print("4. Actualizar Cita.")
            print("5. Consultar Historial.")
            print("6. Salir.")
            
            opcion = int(input("Por favor ingrese una opción: ").strip())
            
            if opcion == 1:
                self.registrarCliente()
            elif opcion == 2:
                self.registrarMascota()
            elif opcion == 3:
                self.programarCita()
            elif opcion == 4:
                self.actualizarCita()
            elif opcion == 5:
                self.consultarHistorial()
            elif opcion == 6:
                print("Gracias por utilizar nuestro sistema. Hasta pronto!!")
                break
            else:
                print("La opcion ingresada no es valida. Por favor intente de nuevo.")    
            
            
if __name__ == "__main__":
    sistema = SistemaVeterinaria()
    sistema.iniciar()