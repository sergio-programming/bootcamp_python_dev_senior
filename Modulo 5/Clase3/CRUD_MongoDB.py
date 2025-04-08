from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

uri = "mongodb+srv://root:admin@cluster0.42fz9ia.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
cliente = MongoClient(uri, server_api=ServerApi('1'))

# Elegir una base de datos y coleccion
db = cliente["mibase"]
coleccion = db["usuarios"]

#Crear 
def crearUsuario(nombre, edad):
    coleccion.insert_one({
        "nombre": nombre,
        "edad": edad
    })
    print("Usuario creado exitosamente")
    
#crearUsuario("Sergio", 36)
#crearUsuario("Laura", 27)

# Funcion para mostrar usuarios
def mostrarUsuarios():
    for usuario in coleccion.find():
        print(usuario)
        
mostrarUsuarios()

# Funcion para actualizar usuarios
def actualizarUsuario(id_str, nuevoNombre, nuevaEdad):
    
    nuevosDatos = {}
    
    if nuevoNombre: nuevosDatos["nombre"] = nuevoNombre
    if nuevaEdad: nuevosDatos["edad"] = nuevaEdad
    
    if not nuevosDatos:
        print("No hay datos para actualizar")
        return
    
    resultado = coleccion.update_one(
        {"_id": ObjectId(id_str)},
        {"$set": nuevosDatos},
    )
    if resultado.modified_count > 0:
        print("Usuario actualizado exitosamente")
        
def eliminarUsuario(id_str):
    coleccion.delete_one({"_id": ObjectId(id_str)})
    print("Usuario eliminado exitosamente")