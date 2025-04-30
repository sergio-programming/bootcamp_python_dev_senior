from controllers.cursos_controller import CursoController
from controllers.profesores_controller import ProfesorController
from textwrap import dedent

controller_cursos = CursoController()
controller_profesores = ProfesorController()

def viewRegistrarCurso():
    print()
    print("#"*30)
    print("MODULO DE REGISTRO DE CURSO")
    print("#"*30)
    
    try:
        nombre = input("\nPor favor ingrese el nombre del curso: ").strip()
        descripcion = input("Por favor ingrese la descripción del curso: ").strip()
        duracion_horas = int(input("Por favor ingrese la duración en horas del curso: ").strip())
        profesor_id = int(input("Por favor ingrese el numero de ID del profesor que dicta el curso: ").strip())
        
        if not nombre or not descripcion or not duracion_horas or not profesor_id:
            raise ValueError("Todos los campos son obligatorios.")
        
        controller_cursos.registrarCursoController(nombre, descripcion, duracion_horas, profesor_id)
        print("\nCurso registrado exitosamente.")
        
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nError inesperado: {e}")
        

def viewConsultarCursos():
    print()
    print("#"*30)
    print("MODULO DE CONSULTA DE CURSOS")
    print("#"*30)
    
    try:
        cursos = controller_cursos.consultarCursosController()
        
        print("\nLISTA DE CURSOS REGISTRADOS:")
        for curso in cursos:
            print(dedent(f"""
            ID: {curso.id_curso}
            Nombre: {curso.nombre}
            Descipción: {curso.descripcion}
            Horas de Duración: {curso.duracion_horas}
            ID Profesor: {curso.profesor_id}
            Nombre Profesor: {curso.nombre_profesor}"""))
        
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nError inesperado: {e}")
        
        
def viewConsultarCurso():
    print()
    print("#"*30)
    print("MODULO DE CONSULTA DE CURSO")
    print("#"*30)
    
    try:
        id_curso = int(input("\nPor favor ingrese el id del curso a consultar: ").strip())
        
        if id_curso <= 0:
            raise ValueError("El id debe ser un numero entero positivo.")
        
        curso = controller_cursos.consultarCursoController(id_curso)
        
        print("\nCURSO CONSULTADO:")
        print(dedent(f"""
        ID: {curso.id_curso}
        Nombre: {curso.nombre}
        Descripción: {curso.descripcion}
        Horas de Duración: {curso.duracion_horas}
        ID Profesor: {curso.profesor_id}
        Nombre Profesor: {curso.nombre_profesor}"""))
        
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nError inesperado: {e}")    
    
def viewActualizarCurso():
    print()
    print("#"*30)
    print("MODULO DE ACTUALIZACIÓN DE CURSO")
    print("#"*30)
    
    try:
        id_curso = int(input("\nPor favor ingrese el id del curso a actualizar: ").strip())
        
        if id_curso <= 0:
            raise ValueError("El id debe ser un numero entero positivo.")
        
        curso_a_actualizar = controller_cursos.consultarCursoController(id_curso)
        
        nombre = input("\nPor favor ingrese el nombre del curso: ").strip()
        if not nombre:
            nombre = curso_a_actualizar.nombre
        
        descripcion = input("Por favor ingrese la descripción del curso: ").strip()
        if not descripcion:
            descripcion = curso_a_actualizar.descripcion
        
        duracion_horas = int(input("Por favor ingrese la duración en horas del curso: ").strip())
        if not duracion_horas:
            duracion_horas = curso_a_actualizar.duracion_horas
        
        profesor_id = int(input("Por favor ingrese el numero de ID del profesor que dicta el curso: ").strip())
        if profesor_id <= 0:
            raise ValueError("El id del profesor debe ser un numero entero positivo.")
        
        if not profesor_id:
            profesor_id = curso_a_actualizar.profesor_id
            
        controller_profesores.consultarProfesorController(profesor_id)        
        
        controller_cursos.actualizarCursoController(id_curso, nombre, descripcion, duracion_horas, profesor_id)
        print("\nCurso actualizado exitosamente.")
    
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nError inesperado: {e}")
        
def viewEliminarCurso():
    print()
    print("#"*30)
    print("MODULO DE ELIMINACIÓN DE CURSO")
    print("#"*30)
    
    try:
        id_curso = int(input("\nPor favor ingrese el id del curso a eliminar: ").strip())
        
        if id_curso <= 0:
            raise ValueError("El id debe ser un numero entero positivo.")
        
        eliminado = controller_cursos.eliminarCursoController(id_curso)
        if eliminado:
            print(f"\nCurso con ID {id_curso} eliminado exitosamente.")
    
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nError inesperado: {e}")
        
def menuCursosView():
    while True:
        print()
        print("#"*30)
        print("MODULO DE GESTIÓN DE CURSOS")
        print("#"*30)
        print(dedent(f"""
        1. Registrar un Curso.
        2. Consultar Cursos.
        3. Consultar un Curso.
        4. Actualizar un Curso.
        5. Eliminar un Curso.
        6. Salir."""))
        
        try:
            opcion = int(input("\nIngrese una opción: ").strip())
            
            if opcion <= 0:
                raise ValueError("La opción debe ser un numero entero positivo.")
            
            if opcion == 1:
                viewRegistrarCurso()
                
            elif opcion == 2:
                viewConsultarCursos()
                
            elif opcion == 3:
                viewConsultarCurso()
                
            elif opcion == 4:
                viewActualizarCurso()
                
            elif opcion == 5:
                viewEliminarCurso()
                
            elif opcion == 6:
                break
            
            else:
                print("La opcion ingresada no es valida. Por favor intente de nuevo.")
                input("Presione <Enter> para continuar")  
            
        except ValueError as e:
            print(f"\nError: {e}")
        except Exception as e:
            print(f"\nError inesperado: {e}")