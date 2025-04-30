from config.conexion import Connection, EjecutarQuerySQL, ObtenerResultadosSQL
from models.cursos import Curso

class CursoController:
    
    def registrarCursoController(self, nombre, descripcion, duracion_horas, profesor_id):
        
        try:
            conexion = Connection()
            query = "INSERT INTO cursos (nombre, descripcion, duracion_horas, profesor_id) VALUES (%s, %s, %s, %s)"
            valores = (nombre, descripcion, duracion_horas, profesor_id)
            ejecutar = EjecutarQuerySQL(conexion)
            ejecutar.execute(query, valores)
        except Exception as e:
            print(f"Error al registrar el curso: {e}")
            raise
        finally:
            conexion.cerrarConexion()
            
    def consultarCursosController(self):
        try:
            conexion = Connection()
            query = "SELECT c.id_curso, c.nombre, c.descripcion, c.duracion_horas, c.profesor_id, CONCAT(p.nombre, ' ', p.apellido) FROM cursos c JOIN profesores p ON c.profesor_id = p.id_profesor;"
            ejecutar = EjecutarQuerySQL(conexion)
            ejecutar.execute_sin_commit(query, valores=())
            resultados = ObtenerResultadosSQL(conexion).fetchall()
            cursos = [Curso(*resultado) for resultado in resultados]
        
            if not cursos:
                raise ValueError("No hay cursos registrados actualmente.")
            
            return cursos
            
        except Exception as e:
            raise
        finally:
            conexion.cerrarConexion()
            
    def consultarCursoController(self, id_curso):
        try:
            conexion = Connection()
            query = """SELECT c.id_curso, c.nombre, c.descripcion, c.duracion_horas, c.profesor_id, CONCAT(p.nombre, ' ', p.apellido)
                    FROM cursos c
                    JOIN profesores p ON c.profesor_id = p.id_profesor
                    WHERE c.id_curso = %s;""" 
            valores = (id_curso,)
            ejecutar = EjecutarQuerySQL(conexion)
            ejecutar.execute_sin_commit(query, valores)
            curso = ObtenerResultadosSQL(conexion).fetchone()                        
            if not curso:
                raise ValueError(f"No hay un curso registrado con el id {id_curso}")
            
            return Curso(*curso)
            
        except Exception as e:
            raise
        finally:
            conexion.cerrarConexion()
            
    def actualizarCursoController(self, id_curso, nombre, descripcion, duracion_horas, profesor_id):
        try:
            conexion = Connection()
            self.consultarCursoController(id_curso)
            
            query = "UPDATE cursos SET nombre = %s, descripcion = %s, duracion_horas = %s, profesor_id = %s WHERE id_curso = %s"
            valores = (nombre, descripcion, duracion_horas, profesor_id, id_curso)
            ejecutar = EjecutarQuerySQL(conexion)
            ejecutar.execute(query, valores)
        except Exception as e:
            raise
        finally:
            conexion.cerrarConexion()
            
    def eliminarCursoController(self, id_curso):
        try:
            conexion = Connection()
            
            self.consultarCursoController(id_curso)
            
            query = "DELETE FROM cursos WHERE id_curso = %s"
            valores = (id_curso,)
            ejecutar = EjecutarQuerySQL(conexion)
            ejecutar.execute(query, valores)
            return True         
        except Exception as e:
            raise
        
        finally:
            conexion.cerrarConexion()