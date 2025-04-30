from controllers.horarios_controller import HorarioController
from controllers.cursos_controller import CursoController
from datetime import datetime
from textwrap import dedent

controller_horarios = HorarioController()
controller_cursos = CursoController()
dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

def viewRegistrarHorario():
    print()
    print("#"*30)
    print("MODULO DE REGISTRO DE HORARIO")
    print("#"*30)
    
    try:
        curso_id = int(input("\nPor favor ingrese el id del curso: ").strip())
        
        if curso_id <= 0:
            raise ValueError("El id del curso debe ser un numero entero positivo.")
        
        controller_cursos.consultarCursoController(curso_id)
        
        dia_semana = input("\nPor favor ingrese el dia de la realizacion de la clase (Lunes/Martes/Miércoles/Jueves/Viernes): ").strip().capitalize()
        
        if not dia_semana in dias_semana:
            raise ValueError("Debe escribir un dia de Lunes a Viernes")            
        
        hora_inicio = input("Por favor ingrese la hora de inicio de la clase (HH:MM): ").strip()
        try:
            datetime.strptime(hora_inicio, "%H:%M")
        except ValueError:
            raise ValueError("La hora debe estar en formato HH:MM.")
                    
        hora_fin = input("Por favor ingrese la hora de finalización de la clase (HH:MM): ").strip()
        try:
            datetime.strptime(hora_fin, "%H:%M")
        except ValueError:
            raise ValueError("La hora debe estar en formato HH:MM.")
            
        controller_horarios.registrarHorarioController(curso_id, dia_semana, hora_inicio, hora_fin)
        print("\nHorario registrado exitosamente")
        
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nError inesperado: {e}")
        
        
def viewConsultarHorarios():
    print()
    print("#"*30)
    print("MODULO DE CONSULTA DE HORARIOS")
    print("#"*30)
    
    try:
        horarios = controller_horarios.consultarHorariosController()
        
        print(f"\nLISTA DE HORARIOS REGISTRADOS")
        for horario in horarios:
            print(dedent(f"""
            ID Horario: {horario.id_horario}
            ID Curso: {horario.curso_id}
            Nombre Curso: {horario.nombre_curso}
            Dia de clase: {horario.dia_semana}
            Hora de inicio: {horario.hora_inicio}
            Hora de finalización: {horario.hora_fin}"""))
        
    except ValueError as e:
        print(f"\nError: {e}")
        
    except Exception as e:
        print(f"\nError inesperado: {e}")
        
def viewConsultarHorario():
    print()
    print("#"*30)
    print("MODULO DE CONSULTA DE HORARIOS")
    print("#"*30)
    
    try:
        id_horario = int(input("Por favor ingrese el id del horario a consultar: ").strip())
        
        if id_horario <= 0:
            raise ValueError("El id del horario debe ser un numero entero positivo")
        
        horario = controller_horarios.consultarHorarioController(id_horario)
        
        print("\nHORARIO CONSULTADO:")
        print(dedent(f"""
        ID Horario: {horario.id_horario}
        ID Curso: {horario.curso_id}
        Nombre Curso: {horario.nombre_curso}
        Dia de clase: {horario.dia_semana}
        Hora de inicio: {horario.hora_inicio}
        Hora de finalización: {horario.hora_fin}"""))
        
    except ValueError as e:
        print(f"\nError: {e}")
        
    except Exception as e:
        print(f"\nError inesperado: {e}")
        
def viewActualizarHorario():
    print()
    print("#"*30)
    print("MODULO DE ACTUALIZACION DE HORARIO")
    print("#"*30)
    
    try:
        id_horario = int(input("\nPor favor ingrese el id del horario a actualizar: ").strip())
        
        if id_horario <= 0:
            raise ValueError("El id del horario debe ser un numero entero positivo")
        
        horario_a_actualizar = controller_horarios.consultarHorarioController(id_horario)
        
        curso_id = int(input("\nPor favor ingrese el id del curso: ").strip())
        if not curso_id:
            curso_id = horario_a_actualizar.curso_id
        
        if curso_id <= 0:
            raise ValueError("El id del horario debe ser un numero entero positivo")
        
        controller_cursos.consultarCursoController(curso_id)
        
        dia_semana = input("Por favor ingrese el dia de la realizacion de la clase(Lunes/Martes/Miércoles/Jueves/Viernes): ").strip().capitalize() or horario_a_actualizar.dia_semana
        
        if dia_semana not in dias_semana:
            raise ValueError("Debe escribir un dia de Lunes a Viernes")
        
        hora_inicio = input("Por favor ingrese la hora de inicio de la clase (HH:MM): ") or horario_a_actualizar.hora_inicio
        
        try:
            datetime.strptime(hora_inicio, "%H:%M")
        except ValueError:
            raise ValueError("La hora debe estar en formato HH:MM.")
            
        hora_fin = input("Por favor ingrese la hora de finalización de la clase (HH:MM): ") or horario_a_actualizar.hora_fin
        
        try:
            datetime.strptime(hora_fin, "%H:%M")
        except ValueError:
            raise ValueError("La hora debe estar en formato HH:MM.")
        
        if hora_inicio >= hora_fin:
            raise ValueError("La hora de inicio debe ser anterior a la hora de finalización.")
            
        controller_horarios.actualizarHorarioController(id_horario, curso_id, dia_semana, hora_inicio, hora_fin)
        print(f"\nHorario con id {id_horario} actualizado exitosamente")        
        
    except ValueError as e:
        print(f"\nError: {e}")
        
    except Exception as e:
        print(f"\nError inesperado: {e}")
        
        
def viewEliminarHorario():
    print()
    print("#"*30)
    print("MODULO DE ELIMINACIÓN DE HORARIO")
    print("#"*30)
    
    try:
        id_horario = int(input("\nPor favor ingrese el id del horario a eliminar: ").strip())
        
        if id_horario <= 0:
            raise ValueError("El id del horario debe ser un numero entero positivo.")
        
        eliminado = controller_horarios.eliminarHorarioController(id_horario)
        if eliminado:
            print(f"\nHorario con id {id_horario} eliminado exitosamente")
        
    except ValueError as e:
        print(f"\nError: {e}")
        
    except Exception as e:
        print(f"\nError inesperado: {e}")
        

def menuHorariosView():
    while True:
        print()
        print("#"*30)
        print("MODULO DE GESTIÓN DE HORARIOS")
        print("#"*30)
        print(dedent("""
        1. Registrar un Horario.
        2. Consultar Horarios.        
        3. Consultar un Horario.
        4. Actualizar un Horario.
        5. Eliminar un Horario.
        6. Salir."""))
        
        try:
            opcion = int(input("\nIngrese una opcion: ").strip())
            
            if opcion <= 0:
                raise ValueError("La opcion debe ser un numero entero positivo.")
            
            if opcion == 1:
                viewRegistrarHorario()
                
            elif opcion == 2:
                viewConsultarHorarios()
                
            elif opcion == 3:
                viewConsultarHorario()
                
            elif opcion == 4:
                viewActualizarHorario()
                
            elif opcion == 5:
                viewEliminarHorario()
                
            elif opcion == 6:
                break
            
        except ValueError as e:
            print(f"\nError: {e}")
        except Exception as e:
            print(f"\nError inesperado: {e}")