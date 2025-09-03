from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

uri = "mongodb+srv://root:admin@cluster0.42fz9ia.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
cliente = MongoClient(uri, server_api=ServerApi('1'))

# Elegir una base de datos y coleccion
db = cliente["mibase"]
coleccion = db["usuarios"]

# CRUD CON MONGO DB

# Funcion para crear usuarios
def crearUsuario(nombre, edad, ciudad):
    coleccion.insert_one({
        "nombre": nombre,
        "edad": edad,
        "ciudad": ciudad
    })
    print("Usuario creado exitosamente")
    
#crearUsuario("Sergio", 36, "Bogotá")
#crearUsuario("Laura", 27, "Medellín")
#crearUsuario("Carlos", 42, "Cali")
#crearUsuario("Andrea", 31, "Barranquilla")
#crearUsuario("Javier", 29, "Cartagena")
#crearUsuario("Paula", 24, "Manizales")
#crearUsuario("Daniel", 33, "Pereira")
#crearUsuario("Camila", 30, "Bucaramanga")
#crearUsuario("Mateo", 22, "Ibagué")
#crearUsuario("Valentina", 26, "Santa Marta")
#crearUsuario("Felipe", 40, "Neiva")
#crearUsuario("Diana", 35, "Cúcuta")
#crearUsuario("Alejandro", 28, "Villavicencio")
#crearUsuario("Natalia", 32, "Armenia")
#crearUsuario("Esteban", 25, "Popayán")
#crearUsuario("Juliana", 34, "Tunja")
#crearUsuario("Samuel", 38, "Sincelejo")
#crearUsuario("Isabela", 23, "Montería")
#crearUsuario("Andrés", 39, "Palmira")
#crearUsuario("Luisa", 21, "Pasto")
#crearUsuario("Mariana", 29, "Bogotá")
#crearUsuario("Juan", 31, "Medellín")
#crearUsuario("Tatiana", 26, "Cali")
#crearUsuario("Nicolás", 34, "Barranquilla")
#crearUsuario("Santiago", 28, "Cartagena")
#crearUsuario("Gabriela", 30, "Manizales")
#crearUsuario("David", 27, "Bucaramanga")
#crearUsuario("Lorena", 33, "Pereira")#

# Funcion para mostrar usuarios
def mostrarUsuarios():
    usuarios = list(coleccion.find())
    if usuarios:
        for i, usuario in enumerate (usuarios, start=1):
            print(f"Usuario #{i}: {usuario}")
    else:
        print("No hay usuarios registrados")


# Funcion para actualizar usuarios
def actualizarUsuario(id_str, nuevoNombre, nuevaEdad):
    
    # Creamos un diccionario con los atributos actualizados
    nuevosDatos = {}
    
    # Si hay valor en la variable nuevoNombre se agrega a la clave nombre del diccionario
    if nuevoNombre: nuevosDatos["nombre"] = nuevoNombre
    # Si hay valor en la variable nuevoNombre se agrega a la clave nombre del diccionario 
    if nuevaEdad: nuevosDatos["edad"] = nuevaEdad
    
    # Si no hay datos en el diccionario se muestra el mensaje
    if not nuevosDatos:
        print("No hay datos para actualizar")
        return
    
    # En la variable resultado alamcenamos la query de Mongo para actualizar
    resultado = coleccion.update_one(
        {"_id": ObjectId(id_str)},
        {"$set": nuevosDatos},
    )
    if resultado.modified_count > 0:
        print("Usuario actualizado exitosamente")
        
#actualizarUsuario("67ef47dc5459ebabc6dd584d", "Angie", 21)
 
# Funcion para eliminar usuario        
def eliminarUsuario(id_str):
    coleccion.delete_one({"_id": ObjectId(id_str)})
    print("Usuario eliminado exitosamente")
    
#eliminarUsuario("67ef4607a0c2c2a815d886b7")

#mostrarUsuarios()

def buscarPorCiudad(ciudad):
    usuarios = coleccion.find({"ciudad": ciudad})
    print("ESTOS SON LOS USUARIOS DE BOGOTA:")
    if usuarios:
        for usuario in usuarios:
            print(usuario)
    else:
        print(f"No hay usuarios registrados en la ciudad de {ciudad}")
        
#buscarPorCiudad("Bogotá")
            
def buscarMayoresA(edad):
    usuarios = coleccion.find({"edad": { "$gt": edad}})
    print("ESTOS SON LOS USUARIOS MAYORES A 30:")
    if usuarios:
        for busqueda in usuarios:
            print(busqueda)
    else:
        print(f"No hay usuarios que tengan mas de {edad} años")
        
#buscarMayoresA(30)      

def buscarMenoresIgualesA(edad):
    usuarios = coleccion.find({"edad": {"$lte": edad}})  
    print("ESTOS SON LOS USUARIOS MENORES O IGUALES A 30:")    
    if usuarios:
        for busqueda in usuarios:
            print(busqueda)
    else:
        print(f"No hay usuarios cuya edad es menor o igual a {edad} años")
        
#buscarMenoresIgualesA(30)

def buscarPorRangoDeEdad(edad_minima, edad_maxima):
    usuarios = coleccion.find({"edad": {"$gt": edad_minima, "$lt": edad_maxima}})
    print(f"ESTOS SON LOS USUARIOS ENTRE {edad_minima} y {edad_maxima} AÑOS:")
    if usuarios:
        for busqueda in usuarios:
            print(busqueda)
    else:
        print("No hay usuarios en ese rango de edad")
        
#buscarPorRangoDeEdad(25, 35)

def buscarPorDosCiudades(ciudad1, ciudad2):
    usuarios = coleccion.find({"$or": [{"ciudad": ciudad1}, {"ciudad": ciudad2}]})
    print(f"ESTOS SON LOS USUARIOS QUE VIVEN EN {ciudad1} y {ciudad2}:")
    if usuarios:
        for busqueda in usuarios:
            print(busqueda)
    else:
        print(f"No hay usuarios que vivan en {ciudad1} y {ciudad2}")
        
buscarPorDosCiudades("Bogotá", "Medellín")