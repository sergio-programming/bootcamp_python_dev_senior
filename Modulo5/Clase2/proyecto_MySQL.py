import mysql.connector


class ConexionMySQL:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.conexion = mysql.connector.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            database = self.database
        )
        self.cursor = self.conexion.cursor()
        
        if self.conexion.is_connected():      
            print("Conexion establecida con MySQL")
            
    def cerrarConexion(self):
        self.cursor.close()
        self.conexion.close()
        print("Se ha cerrado la conexion con MySQL")
        
    def ejecutarQuery(self, query, parametros: tuple):
        self.cursor.execute(query, parametros)
        self.conexion.commit()
    
    def mostrarResultados(self):
        return self.cursor.fetchall()

class GestionProfesores:
    def __init__(self, conexion: ConexionMySQL):
        self.conexion = conexion
    
    def mostrarProfesores(self):
        self.conexion.cursor.execute("SELECT *FROM profesores")
        resultados = self.conexion.mostrarResultados()
        if not resultados:
            print("No hay profesores registrados actualmente")
        else:
            print("PROFESORES REGISTRADOS")
            for i, resultado in enumerate(resultados, start=1):
                print(f"Profesor #{i}: {resultado}")
                
    def crearProfesor(self, nombre, especialidad, experiencia):
        query = "INSERT INTO profesores (nombre, especialidad, experiencia) values (%s, %s, %s)"
        valores = (nombre, especialidad, experiencia)
        self.conexion.ejecutarQuery(query, valores)
        print("Registro de profesor exitoso")   
            
def main():
    db_sql = ConexionMySQL("localhost", 3306, "root", "admin", "academiadevsenior")
    gestionProfesores = GestionProfesores(db_sql)
    gestionProfesores.crearProfesor("Cesar Diaz", "Java", 14)
    gestionProfesores.mostrarProfesores() 
    
    
main()