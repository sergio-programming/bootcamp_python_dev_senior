from controllers.matriculas_controller import MatriculaController
from controllers.cursos_controller import CursoController
from controllers.estudiantes_controller import EstudianteController
from textwrap import dedent
from datetime import datetime

controller_matriculas = MatriculaController()
controller_estudiantes = EstudianteController()
controller_cursos = CursoController()

def viewRegistrarMatricula():
    print()
    print("#"*30)
    print("MODULO DE REGISTRO DE MATRICULA")
    print("#"*30)
    
    try:
        estudiante_id = int(input("\nPor favor ingrese el id del estudiante: ").strip())
        
        if estudiante_id <= 0:
            raise ValueError("El id debe ser un numero entero positivo.")
        
        controller_estudiantes.consultarEstudianteController(estudiante_id)
        
        curso_id = int(input("\nPor favor ingrese el id del curso: ").strip())
        
        if curso_id <= 0:
            raise ValueError("El id del curso debe ser un numero entero positivo.")
        
        controller_cursos.consultarCursoController(curso_id)
        
        fecha_matricula = input("\nPor favor ingrese la fecha de matricula (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(fecha_matricula, "%Y-%m-%d")
        except ValueError:
            print("La fecha debe estar en formato YYYY-MM-DD.")
                  
        
        controller_matriculas.registrarMatriculaController(estudiante_id, curso_id, fecha_matricula)        
        print("\nMatricula registrada exitosamente.")
               
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nError inesperado: {e}")
        

def viewConsultarMatriculas():
    print()
    print("#"*30)
    print("MODULO DE CONSULTA DE MATRICULAS")
    print("#"*30)
    
    try:
        matriculas = controller_matriculas.consultarMatriculasController()
        
        print("\nLISTA DE MATRICULAS REGISTRADAS:")
        for matricula in matriculas:
            print(dedent(f"""
            ID: {matricula.id_matricula}
            ID Estudiante: {matricula.estudiante_id}
            Nombre Estudiante: {matricula.estudiante_nombre}
            ID Curso: {matricula.curso_id}
            Nombre Curso: {matricula.curso_nombre}
            Fecha Matricula: {matricula.fecha_matricula}"""))
        
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
        
        
def viewConsultarMatricula():
    print()
    print("#"*30)
    print("MODULO DE CONSULTA DE MATRICULA")
    print("#"*30)
    
    try:
        id_matricula = int(input("\nPor favor ingrese el id de la matricula: ").strip())
        
        if id_matricula <= 0:
            raise ValueError("El id debe ser un numero entero positivo.")
        
        matricula = controller_matriculas.consultarMatriculaController(id_matricula)
        
        print(dedent(f"""
        ID: {matricula.id_matricula}
        ID Estudiante: {matricula.estudiante_id}
        Nombre Estudiante: {matricula.estudiante_nombre}
        ID Curso: {matricula.curso_id}
        Nombre Curso: {matricula.curso_nombre}
        Fecha Matricula: {matricula.fecha_matricula}"""))
        
    except ValueError as e:
        print(f"\nError: {e}")  
    except Exception as e:
        print(f"Error inesperado: {e}")
    
    
def viewActualizarMatricula():
    print()
    print("#"*30)
    print("MODULO DE ACTUALIZACIÓN DE MATRICULA")
    print("#"*30)
    
    try:
        id_matricula = int(input("\nPor favor ingrese el id de la matricula: ").strip())
        
        if id_matricula <= 0:
            raise ValueError("El id de la matricula debe ser un numero entero positivo.")
        
        matricula_a_actualizar = controller_matriculas.consultarMatriculaController(id_matricula)
        
        estudiante_id = int(input("\nPor favor ingrese el id del estudiante: ").strip())
        
        if estudiante_id <= 0:
            raise ValueError("El id del estudiante debe ser un numero entero positivo.")
        
        controller_estudiantes.consultarEstudianteController(estudiante_id)
        
        curso_id = int(input("\nPor favor ingrese el id del curso: ").strip())
        
        if curso_id <= 0:
            raise ValueError("El id del curso debe ser un numero entero positivo.")
        
        controller_cursos.consultarCursoController(curso_id)
        
        fecha_matricula = input("\nPor favor ingrese la fecha de matricula (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(fecha_matricula, "%Y-%m-%d")
        except ValueError:
            print("La fecha debe estar en formato YYYY-MM-DD.")
        
        controller_matriculas.actualizarMatriculaController(id_matricula, estudiante_id, curso_id, fecha_matricula)
        print(f"\nMatricula con ID {id_matricula} actualizada exitosamente.")
        
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nError inesperado: {e}")
      

def viewEliminarMatricula():
    print()
    print("#"*30)    
    print("MODULO DE ELIMINACIÓN DE MATRICULA")
    print("#"*30)
    
    try:
        id_matricula = int(input("\nPor favor ingrese el id de la matricula: ").strip())
        
        if id_matricula <= 0:
            raise ValueError("El id de la matricula debe ser un numero entero positivo.")
        
        eliminado = controller_matriculas.eliminarMatriculaController(id_matricula)
        if eliminado:
            print(f"\nMatricula con ID {id_matricula} eliminada exitosamente.")
        
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nError inesperado: {e}")   
        
        
def menuMatriculasView():
    while True:
        print()
        print("#"*30)
        print("MODULO DE GESTIÓN DE MATRICULAS")
        print("#"*30)
        print(dedent("""
        1. Registrar una Matricula.
        2. Consultar Matriculas.        
        3. Consultar una Matricula.
        4. Actualizar una Matricula.
        5. Eliminar una Matricula.
        6. Salir."""))
        
        try:
            opcion = int(input("\nIngrese una opcion: ").strip())
            
            if opcion <= 0:
                raise ValueError("La opcion debe ser un numero entero positivo.")
            
            if opcion == 1:
                viewRegistrarMatricula()
                
            elif opcion == 2:
                viewConsultarMatriculas()
                
            elif opcion == 3:
                viewConsultarMatricula()
                
            elif opcion == 4:
                viewActualizarMatricula()
                
            elif opcion == 5:
                viewEliminarMatricula()
                
            elif opcion == 6:
                break
            
        except ValueError as e:
            print(f"\nError: {e}")
        except Exception as e:
            print(f"\nError inesperado: {e}")