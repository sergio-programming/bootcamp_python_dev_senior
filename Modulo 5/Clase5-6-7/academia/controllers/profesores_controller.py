from config.conexion import Connection, EjecutarQuerySQL, ObtenerResultadosSQL
from models.profesores import Profesor

class ProfesorController:
    
    def registrarProfesorController(self, nombre, apellido, correo_electronico, telefono, especialidad):
        try:
            conexion = Connection()
            query = "INSERT INTO profesores (nombre, apellido, correo_electronico, telefono, especialidad) VALUES (%s, %s, %s, %s, %s)"
            valores = (nombre, apellido, correo_electronico, telefono, especialidad)
            ejecutar = EjecutarQuerySQL(conexion)
            ejecutar.execute(query, valores)
        except Exception as e:
            raise
        finally:
            conexion.cerrarConexion()
            
    def consultarProfesoresController(self):
        try:
            conexion = Connection()
            query = "SELECT *FROM profesores"
            ejecutar = EjecutarQuerySQL(conexion)
            ejecutar.execute_sin_commit(query, valores=())
            resultados = ObtenerResultadosSQL(conexion).fetchall()
            profesores = [Profesor(*resultado) for resultado in resultados]
            if not profesores:
                raise ValueError("No hay profesores registrados actualmente")
            return profesores
        
        except Exception as e:
            raise
        finally:
            conexion.cerrarConexion()
            
    def consultarProfesorController(self, id_profesor):
        try:
            conexion = Connection()
            query = "SELECT *FROM profesores WHERE id_profesor = %s"
            valores = (id_profesor,)
            ejecutar = EjecutarQuerySQL(conexion)
            ejecutar.execute_sin_commit(query, valores)
            profesor = ObtenerResultadosSQL(conexion).fetchone()
            if not profesor:
                raise ValueError(f"No hay un profesor registrado con el id {id_profesor}")
            return Profesor(*profesor)
        
        except Exception as e:
            raise
        finally:
            conexion.cerrarConexion()
            
    def actualizarProfesorController(self, id_profesor, nombre, apellido, correo_electronico, telefono, especialidad):
        try:
            conexion = Connection()
            
            self.consultarProfesorController(id_profesor)
                        
            query = "UPDATE profesores SET nombre = %s, apellido = %s, correo_electronico = %s, telefono = %s, especialidad = %s WHERE id_profesor = %s"
            valores = (nombre, apellido, correo_electronico, telefono, especialidad, id_profesor)
            ejecutar = EjecutarQuerySQL(conexion)
            ejecutar.execute(query, valores)
        except Exception as e:
            raise    
        finally:                
            conexion.cerrarConexion()
            
    def eliminarProfesorController(self, id_profesor):
        try:
            conexion = Connection()
            
            self.consultarProfesorController(id_profesor)
            
            query = "DELETE FROM profesores WHERE id_profesor = %s"
            valores = (id_profesor,)
            ejecutar = EjecutarQuerySQL(conexion)
            ejecutar.execute(query, valores)
            return True
        except Exception as e:
            raise
        finally:
            conexion.cerrarConexion()