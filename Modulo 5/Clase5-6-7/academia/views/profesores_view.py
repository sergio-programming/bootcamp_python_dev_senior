from controllers.profesores_controller import ProfesorController
from textwrap import dedent

controller_profesores = ProfesorController()

def viewRegistrarProfesor():
    print()
    print("#"*30)
    print("MODULO DE REGISTRO DE UN PROFESOR")
    print("#"*30)
    
    try:
        nombre = input("\nPor favor ingrese el nombre del profesor: ").strip()
        apellido = input("Por favor ingrese el apellido del profesor: ").strip()
        correo_electronico = input("Por favor ingrese el correo electronico del profesor: ").strip()
        telefono = input("Por favor ingrese el telefono del profesor: ").strip()
        especialidad = input("Por favor ingrese la especialidad del profesor: ").strip()
        
        if not nombre or not apellido or not correo_electronico or not telefono or not especialidad:
            raise ValueError("Todos los campos son obligatorios.")
        
        controller_profesores.registrarProfesorController(nombre, apellido, correo_electronico, telefono, especialidad)
        print("\nProfesor registrado exitosamente.")
        
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
        
def viewConsultarProfesores():
    print()
    print("#"*30)
    print("MODULO DE CONSULTA DE PROFESORES")
    print("#"*30)
    
    try:
        profesores = controller_profesores.consultarProfesoresController()
        
        print("\nLISTA DE PROFESORES REGISTRADOS:")
        for profesor in profesores:
            print(dedent(f"""
            ID: {profesor.id_profesor}
            Nombre: {profesor.nombre}
            Apellido: {profesor.apellido}
            Correo Electronico: {profesor.correo_electronico}
            Telefono: {profesor.telefono}
            Especialidad: {profesor.especialidad}"""))
        
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nError inesperado: {e}")
        
def viewConsultarProfesor():
    print()
    print("#"*30)
    print("MODULO DE CONSULTA DE UN PROFESOR")
    print("#"*30)
    
    try:
        id_profesor = int(input("\nPor favor ingrese el id del profesor a consultar: ").strip())
        
        if id_profesor <= 0:
            raise ValueError("El id debe ser un numero entero positivo.")
        
        profesor = controller_profesores.consultarProfesorController(id_profesor)       
        
        print("\nPROFESOR CONSULTADO:")
        print(dedent(f"""
        ID: {profesor.id_profesor}
        Nombre: {profesor.nombre}
        Apellido: {profesor.apellido}
        Correo Electronico: {profesor.correo_electronico}
        Telefono: {profesor.telefono}
        Especialidad: {profesor.especialidad}"""))
        
        
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nError inesperado: {e}")
        
def viewActualizarProfesor():
    print()
    print("#"*30)
    print("MODULO DE ACTUALIZACIÓN DE UN PROFESOR")
    print("#"*30)
    
    try:
        id_profesor = int(input("Por favor ingrese el id del profesor a actualizar: ").strip())
        
        if id_profesor <= 0:
            raise ValueError("El id debe ser un numero entero positivo")
        
        profesor_a_actualizar = controller_profesores.consultarProfesorController(id_profesor)
        
        nombre = input("\nPor favor ingrese el nombre del profesor: ").strip()
        if not nombre:
            nombre = profesor_a_actualizar.nombre
        
        apellido = input("Por favor ingrese el apellido del profesor: ").strip()
        if not apellido:
            apellido = profesor_a_actualizar.apellido
            
        correo_electronico = input("Por favor ingrese el correo electronico del profesor: ").strip()
        if not correo_electronico:
            correo_electronico = profesor_a_actualizar.correo_electronico
        
        telefono = input("Por favor ingrese el telefono del profesor: ").strip()
        if not telefono:
            telefono = profesor_a_actualizar.telefono
        
        especialidad = input("Por favor ingrese la especialidad del profesor: ").strip()
        if not especialidad:
            especialidad = profesor_a_actualizar.especialidad
            
        controller_profesores.actualizarProfesorController(id_profesor, nombre, apellido, correo_electronico, telefono, especialidad)
        print("\nProfesor actualizado exitosamente.")        
        
        
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
        
        
def viewEliminarProfesor():
    print()
    print("#"*30)
    print("MODULO DE ELIMINACIÓN DE UN PROFESOR")
    print("#"*30)
    
    try:
        id_profesor = int(input("\nPor favor ingrese el id del profesor a eliminar: ").strip())
        
        if id_profesor <= 0:
            raise ValueError("El id debe ser un numero entero positivo")
        
        eliminado = controller_profesores.eliminarProfesorController(id_profesor)
        if eliminado:
            print(f"\nProfesor con ID {id_profesor} eliminado exitosamente")
        
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nError inesperado: {e}")
        
        
def menuProfesoresView():
    while True:
        print()
        print("#"*30)
        print("MODULO DE GESTIÓN DE PROFESORES")
        print("#"*30)
        print(dedent(f"""
        1. Registrar un Profesor.
        2. Consultar Profesores.
        3. Consultar un Profesor.
        4. Actualizar un Profesor.
        5. Eliminar un Profesor.
        6. Salir."""))
        
        try:
            opcion = int(input("\nIngrese una opción: ").strip())    
            
            if opcion <= 0:
                raise ValueError("La opción debe ser un numero entero positivo.")
                
            if opcion == 1:
                viewRegistrarProfesor()
                
            elif opcion == 2:
                viewConsultarProfesores()
                
            elif opcion == 3:
                viewConsultarProfesor()
                
            elif opcion == 4:
                viewActualizarProfesor()
                
            elif opcion == 5:
                viewEliminarProfesor()
                
            elif opcion == 6:
                break
                
            else:
                print("La opcion ingresada no es valida. Por favor intente de nuevo.")
                input("Presione <Enter> para continuar")     
            
            
        except ValueError as e:
            print(f"\nError: {e}")
            input("Presione <Enter> para continuar")
        except Exception as e:
            print(f"\nError inesperado: {e}")
            input("Presione <Enter> para continuar")
        
        
        
        