from config.conexion import Connection, EjecutarQuerySQL, ObtenerResultadosSQL
from models.estudiantes import Estudiante

class EstudianteController:
    
    def registrarEstudianteController(self, nombre, apellido, correo_electronico, telefono):
        try:
            conexion = Connection()
            query = "INSERT INTO estudiantes (nombre, apellido, correo_electronico, telefono) VALUES (%s, %s, %s, %s)"
            valores = (nombre, apellido, correo_electronico, telefono)
            ejecutar = EjecutarQuerySQL(conexion)
            ejecutar.execute(query, valores)
        except Exception as e:
            raise
        finally:
            conexion.cerrarConexion()
    
    def consultarEstudiantesController(self):
        try:
            conexion = Connection()
            ejecutar = EjecutarQuerySQL(conexion)
            query = "SELECT * FROM estudiantes" 
            ejecutar.execute_sin_commit(query, valores=())          
            resultados = ObtenerResultadosSQL(conexion).fetchall()
            estudiantes = [Estudiante(*resultado) for resultado in resultados]                
            if not estudiantes:
                raise ValueError("No hay estudiantes registrados actualmente")
            return estudiantes
                   
        except Exception as e:
            raise
        finally:
            conexion.cerrarConexion()  
    
    def consultarEstudianteController(self, id_estudiante):
        try:
            conexion = Connection()
            ejecutar = EjecutarQuerySQL(conexion)
            query = "SELECT * FROM estudiantes WHERE id_estudiante = %s"
            valores = (id_estudiante,)
            ejecutar.execute_sin_commit(query, valores)
            estudiante = ObtenerResultadosSQL(conexion).fetchone()
            if not estudiante:
                raise ValueError(f"No hay un estudiante registrado con el id {id_estudiante}")
            return Estudiante(*estudiante)
    
        except Exception as e:  
            raise
        finally:
            conexion.cerrarConexion()

    def actualizarEstudianteController(self, id_estudiante, nombre, apellido, correo_electronico, telefono):
        try:
            conexion = Connection()
            
            self.consultarEstudianteController(id_estudiante)
            
            query = "UPDATE estudiantes SET nombre = %s, apellido = %s, correo_electronico = %s, telefono = %s WHERE id_estudiante = %s"
            valores = (nombre, apellido, correo_electronico, telefono, id_estudiante)
            ejecutar = EjecutarQuerySQL(conexion)
            ejecutar.execute(query, valores)
        except Exception as e:
            raise
        finally:
            conexion.cerrarConexion()
            
    def eliminarEstudianteController(self, id_estudiante):
        try:
            conexion = Connection()
            
            self.consultarEstudianteController(id_estudiante)
            
            query = "DELETE FROM estudiantes WHERE id_estudiante = %s"
            valores = (id_estudiante,)
            ejecutar = EjecutarQuerySQL(conexion)
            ejecutar.execute(query, valores)
            return True
        except Exception as e:
            raise
        finally:
            conexion.cerrarConexion()