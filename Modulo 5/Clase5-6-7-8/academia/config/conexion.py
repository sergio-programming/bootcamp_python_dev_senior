import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class Connection:
    def __init__(self):
        self.conexion = mysql.connector.connect (
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME") 
        )
        self.cursor = self.conexion.cursor()
        
    def cerrarConexion(self):
        self.cursor.close()
        self.conexion.close()
        
    def commit(self):
        self.conexion.commit()
        
        
class EjecutarQuerySQL:
    def __init__(self, connection: Connection):
        self.db = connection
        
    def execute(self, query, valores: tuple=()):
        self.db.cursor.execute(query, valores)
        self.db.commit()
        
    def execute_sin_commit(self, query, valores: tuple=()):
        self.db.cursor.execute(query, valores)           
    

class ObtenerResultadosSQL:
    def __init__(self, connection: Connection):
        self.db = connection
        
    def fetchone(self):
        return self.db.cursor.fetchone()
                
    def fetchall(self):
        return self.db.cursor.fetchall()
