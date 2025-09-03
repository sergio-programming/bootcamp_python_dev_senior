#Forma de declara clases
class Persona:
    #Metodo Constructor
    def __init__(self, nombre, apellido, dni, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.edad = edad
        
#Forma de crear instancias de clase
persona1 = Persona("Sergio", "Pedraza", "1032421747", 36)
persona2 = Persona("Luisa", "Rojas", "1045524880", 25)

print(f"Estos son los datos: {persona1}")
print(f"Estos son los datos: {persona2}")
