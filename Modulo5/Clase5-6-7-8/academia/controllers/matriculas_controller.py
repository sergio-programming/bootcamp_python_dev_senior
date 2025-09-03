from config.conexion import Connection, EjecutarQuerySQL, ObtenerResultadosSQL
from models.matriculas import Matricula

class MatriculaController:
    
    def registrarMatriculaController(self, estudiante_id, curso_id, fecha_matricula):
        try:
            conexion = Connection()
            query = "INSERT INTO matriculas (estudiante_id, curso_id, fecha_matricula) VALUES (%s, %s, %s);"
            valores = (estudiante_id, curso_id, fecha_matricula)
            ejecutar = EjecutarQuerySQL(conexion)
            ejecutar.execute(query, valores)
        except Exception as e:
            raise
        finally:        
            conexion.cerrarConexion()
            
    def consultarMatriculasController(self):
        try:
            conexion = Connection()
            query = """SELECT m.id_matricula, m.estudiante_id, CONCAT(e.nombre, ' ', e.apellido), m.curso_id, c.nombre, m.fecha_matricula
                    FROM matriculas m
                    JOIN estudiantes e ON m.estudiante_id = e.id_estudiante
                    JOIN cursos c ON m.curso_id = c.id_curso;"""
            ejecutar = EjecutarQuerySQL(conexion)
            ejecutar.execute_sin_commit(query, valores=())
            resultados = ObtenerResultadosSQL(conexion).fetchall()
            matriculas = [Matricula(*resultado) for resultado in resultados]
            
            if not matriculas:
                raise ValueError("No hay matriculas registradas actualmente.")
            
            return matriculas
        except Exception as e:
            raise
        finally:
            conexion.cerrarConexion()
            
    def consultarMatriculaController(self, id_matricula):
        try:
            conexion = Connection()
            query = """SELECT m.id_matricula, m.estudiante_id, CONCAT(e.nombre, ' ', e.apellido), m.curso_id, c.nombre, m.fecha_matricula
|                   FROM matriculas m
                    JOIN estudiantes e ON m.estudiante_id = e.id_estudiante
                    JOIN cursos c ON m.curso_id = c.id_curso
                    WHERE m.id_matricula = %s;"""
            valores = (id_matricula,)
            ejecutar = EjecutarQuerySQL(conexion)
            ejecutar.execute_sin_commit(query, valores)
            matricula = ObtenerResultadosSQL(conexion).fetchone()
            
            if not matricula:
                raise ValueError(f"No hay una matricula registrada con el id {id_matricula}")
            
            return Matricula(*matricula)
        except Exception as e:
            raise
        finally:
            conexion.cerrarConexion()
            
    def actualizarMatriculaController(self, id_matricula, estudiante_id, curso_id, fecha_matricula):
        try:
            conexion = Connection()
            self.consultarMatriculaController(id_matricula)
            
            query = "UPDATE matriculas SET estudiante_id = %s, curso_id = %s, fecha_matricula = %s WHERE id_matricula = %s;"
            valores = (estudiante_id, curso_id, fecha_matricula, id_matricula)
            ejecutar = EjecutarQuerySQL(conexion)
            ejecutar.execute(query, valores)
        except Exception as e:
            raise
        finally:
            conexion.cerrarConexion()
            
    def eliminarMatriculaController(self, id_matricula):
        try:
            conexion = Connection()
            self.consultarMatriculaController(id_matricula)
            
            query = "DELETE FROM matriculas WHERE id_matricula = %s;"
            valores = (id_matricula,)
            ejecutar = EjecutarQuerySQL(conexion)
            ejecutar.execute(query, valores)
            return True
        except Exception as e:
            raise
        finally:
            conexion.cerrarConexion()