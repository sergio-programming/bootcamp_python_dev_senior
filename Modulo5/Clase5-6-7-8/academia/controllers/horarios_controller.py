from config.conexion import Connection, EjecutarQuerySQL, ObtenerResultadosSQL
from models.horarios import Horario

class HorarioController:
    
    def registrarHorarioController(self, curso_id, dia_semana, hora_inicio, hora_fin):
        try:
            conexion = Connection()
            query = "INSERT INTO horarios (curso_id, dia_semana, hora_inicio, hora_fin) VALUES (%s, %s, %s, %s);"
            valores = (curso_id, dia_semana, hora_inicio, hora_fin)
            ejecutar = EjecutarQuerySQL(conexion)
            ejecutar.execute(query, valores)    
        
        except Exception as e:
            raise
        finally:
            conexion.cerrarConexion()
            
    def consultarHorariosController(self):
        try:
            conexion = Connection()
            query = """SELECT h.id_horario, h.curso_id, h.dia_semana, h.hora_inicio, h.hora_fin, c.nombre
                    FROM horarios h
                    JOIN cursos c ON h.curso_id = c.id_curso;"""
            ejecutar = EjecutarQuerySQL(conexion)
            ejecutar.execute_sin_commit(query, valores=())
            resultados = ObtenerResultadosSQL(conexion).fetchall()
            horarios = [Horario(*resultado) for resultado in resultados]
            
            if not horarios:
                raise ValueError("No hay horarios registrados actualmente.")
            
            return horarios
        except Exception as e:
            raise
        finally:
            conexion.cerrarConexion()
            
    def consultarHorarioController(self, id_horario):
        try:
            conexion = Connection()
            query = """SELECT h.id_horario, h.curso_id, h.dia_semana, h.hora_inicio, h.hora_fin, c.nombre
                    FROM horarios h
                    JOIN cursos c ON h.curso_id = c.id_curso
                    WHERE h.id_horario = %s;"""
            valores = (id_horario,)
            ejecutar = EjecutarQuerySQL(conexion)
            ejecutar.execute_sin_commit(query, valores)
            horario = ObtenerResultadosSQL(conexion).fetchone()
            
            if not horario:
                raise ValueError(f"No hay un horario registrado con el id {id_horario}")
            
            return Horario(*horario)
        except Exception as e:
            raise
        finally:
            conexion.cerrarConexion()
            
    def actualizarHorarioController(self, id_horario, curso_id, dia_semana, hora_inicio, hora_fin):
        try:
            conexion = Connection()
            self.consultarHorarioController(id_horario)
            
            query = "UPDATE horarios SET curso_id = %s, dia_semana = %s, hora_inicio = %s, hora_fin = %s WHERE id_horario = %s;"
            valores = (curso_id, dia_semana, hora_inicio, hora_fin, id_horario)
            ejecutar = EjecutarQuerySQL(conexion)
            ejecutar.execute(query, valores)
        except Exception as e:
            raise
        finally:
            conexion.cerrarConexion()
            
    def eliminarHorarioController(self, id_horario):
        try:
            conexion = Connection()
            self.consultarHorarioController(id_horario)
            
            query = "DELETE FROM horarios WHERE id_horario = %s;"
            valores = (id_horario,)
            ejecutar = EjecutarQuerySQL(conexion)
            ejecutar.execute(query, valores)
            return True
        except Exception as e:
            raise
        finally:
            conexion.cerrarConexion()