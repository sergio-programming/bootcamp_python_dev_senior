import sqlite3
import mysql.connector

# Conexion
class ConexionSQLite:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conexion = sqlite3.connect(db_path)
        self.cursor = self.conexion.cursor()
        print("Conexion establecida con SQLite")
        
    def cerrarConexion(self):
        self.cursor.close()
        self.conexion.close()
        print("Se ha cerrado la conexion con SQLite")
        
    def ejecutarQuery(self, query, parametros: tuple):
        self.cursor.execute(query, parametros)
        self.conexion.commit()
    
    def mostrarResultados(self):
        return self.cursor.fetchall()
    
class GestionTeacher:
    def __init__(self, conexion: ConexionSQLite):
        self.conexion = conexion
        
    def mostrarProfesores(self):
        self.conexion.cursor.execute("SELECT *FROM profesores")
        resultados = self.conexion.mostrarResultados()
        if not resultados:
            print("No hay profesores registrados actualmente")
        else:
            print("PROFESORES REGISTRADOS")
            for i, resultado in enumerate(resultados, start=1):
                print(F"Profesor #{i}: {resultado}")
                
    def crearProfesor(self, nombre, especialidad, experencia):
        query = "INSERT INTO profesores (nombre, especialidad, experiencia) values (?, ?, ?)"
        valores = (nombre, especialidad, experencia)
        self.conexion.ejecutarQuery(query, valores)    
        print("Registro de profesor exitoso") 
        
def main():
    db_sqlite = ConexionSQLite("academiadevsenior.db")
    gestionProfesor = GestionTeacher(db_sqlite)
    gestionProfesor.crearProfesor("Cesar Diaz", "Java", 14)
    gestionProfesor.mostrarProfesores()
    
main()