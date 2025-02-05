#Variable
clientes = []
mascotas = []

#Clases principales
class SistemaVeterinaria:
    class Persona:
        id_counter = 1
        
        def __init__(self,nombre,contacto):
            self.id = SistemaVeterinaria.Persona.id_counter
            self.nombre = nombre
            self.contacto = contacto
            
            SistemaVeterinaria.Persona.id_counter += 1

    class Cliente(Persona):
        def __init__(self, nombre, contacto,direccion):
            super().__init__(nombre, contacto)
            self.direccion = direccion
            self.mascotas = []
            
        def agregar_mascota(self,mascota):
            self.mascotas.append(mascota)

    class Mascota:
        id_counter = 1
        
        def __init__(self,nombre,especie,raza,edad):
            self.id = SistemaVeterinaria.Mascota.id_counter
            self.nombre = nombre 
            self.especie = especie
            self.raza = raza
            self.edad = edad
            self.historia_clinico= []
            
            SistemaVeterinaria.Mascota.id_counter += 1
            
        def agregar_cita(self,cita):
            self.historia_clinico.append(cita)
            
        def mostar_historial(self):
            if not self.historia_clinico:
                print(f"No hay citas registradas para {self.nombre}")
            else:
                print(f"Historial de las citas para {self.nombre}:")
                for cita in self.historia_clinico:
                    print(f" - {cita.fecha} a las {cita.hora}, servicio:: {cita.servicio}, Veterinario: {cita.veterinario}")

    class Cita:
        id_counter = 1
        
        def __init__(self,fecha,hora,servicio,veterinario):
            self.id = SistemaVeterinaria.Cita.id_counter
            self.fecha = fecha
            self.hora = hora
            self.servicio = servicio
            self.veterinario = veterinario
            
            SistemaVeterinaria.Cita.id_counter += 1


#Funciones auxiliares
def validar_fecha(fecha):
    from datetime import datetime
    try:
        datetime.strptime(fecha,"%Y-%m-%d")
        return True
    except ValueError:
        return False


#Funciones del sistemas
def registrar_cliente():
    print("========REGISTRO DE CLIENTE===========")
    nombre = input("Ingrese nombre del cliente: ")
    contacto = input("Ingrese contacto del cliente: ")
    direccion = input("Ingrese la direccion del cliente: ")
    cliente = SistemaVeterinaria.Cliente(nombre,contacto,direccion)
    clientes.append(cliente)
    print(f"Cliente registrado con exito. ID: {cliente.id}")
    
    
def registar_mascota():
    print("=============REGISTRO DE MASCOTA==========")
    
    cliente_id = int(input("Ingrese el ID del Cliente para asociar la mascota: "))
    cliente = next((c for c in clientes if c.id == cliente_id), None)
    
    if not cliente:
        print("Cliente no encontrado.")
        return
    
    
    nombre_mascota= input("Nombre de la mascota: ")
    especie = input("Especie de la mascota: ")
    raza = input("Raza de la mascota: ")
    edad = input("Ingrese edad de la mascota: ")
    mascota = SistemaVeterinaria.Mascota(nombre_mascota,especie,raza,edad)
    
    
    cliente.agregar_mascota(mascota)
    mascotas.append(mascota)
    print(f"Mascota registrada con exito, ID :{mascota.id}")

def programar_cita():
    
    cliente_id = int(input("Ingrese el ID del cliente: "))
    cliente = next((c for c in clientes if c.id == cliente_id), None)
    
    if not cliente:
        print("Cliente no encontrado.")
        return
    
    mascota_id = int(input("Ingrese el ID del mascota: "))
    mascota = next((m for m in cliente.mascotas if m.id == mascota_id), None)
    
    if not mascota:
        print("Mascota no encontrado.")
        return
    
    fecha = input("Ingrese la fecha de la cita(YYYY-MM-DD): ")
    while not validar_fecha(fecha):
        print("Fecha invalida, Por Favor, use el formato YYYY-MM-DD")
        fecha = input("Ingrese la fecha de la cita(YYYY-MM-DD): ")
    hora = input("Ingrese la hora de la cita (HH:MM): ")
    servicio = input("Ingrese el servicio(Consultoria, vacunacion, etc.): ")
    veterinario = input("Ingrese nombre de Veterinario: ")
    
    cita = SistemaVeterinaria.Cita(fecha,hora,servicio,veterinario)
    mascota.agregar_cita(cita)
    print("Cita agendada")

def consultar_historia():
    
    print("Consultar historial de citas")
    
    cliente_id = int(input("Ingrese el ID del cliente: "))
    cliente = next((c for c in clientes if c.id == cliente_id), None)
    
    if not cliente:
        print("Cliente no encontrado.")
        return
    
    mascota_id = int(input("Ingrese el ID del mascota: "))
    mascota = next((m for m in cliente.mascotas if m.id == mascota_id), None)
    
    if not mascota:
        print("Mascota no encontrado.")
        return

    mascota.mostar_historial()
    
#Menu Principal
def menu_principal():
    while True:
        print("==============Menu Principal==============")
        print("1. Registar cliente ")
        print("2. Registar mascota")
        print("3. Programar Cita")
        print("4. Consultar historial de servicios")
        print("5. Salir")
        opc = input("Selecicion una opcion: ")
        
        if opc == "1":
            registrar_cliente()
        elif opc == "2":
            registar_mascota()
        elif opc == "3":
            programar_cita()
        elif opc == "4":
            consultar_historia()
        elif opc == "5":
            break
        else:
            print("Opcion no valida. Intente de nuevo")

menu_principal()