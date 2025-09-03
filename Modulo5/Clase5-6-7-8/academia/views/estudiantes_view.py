from controllers.estudiantes_controller import EstudianteController
from textwrap import dedent

controller_estudiantes = EstudianteController()
  
def viewRegistrarEstudiante():
    print()
    print("#"*30)
    print("MODULO DE REGISTRO DE UN ESTUDIANTE")
    print("#"*30)
    try:
        nombre = input("\nPor favor ingrese el nombre del estudiante: ").strip()
        apellido = input("Por favor ingrese el apellido del estudiante: ").strip()
        correo_electronico = input("Por favor ingrese el correo electronico del estudiante: ").strip()
        telefono = input("Por favor ingrese el numero de telefono del estudiante: ").strip()
        
        if not nombre or not apellido or not correo_electronico or not telefono:
            raise ValueError("Todos los campos son obligatorios.")
        
        controller_estudiantes.registrarEstudianteController(nombre, apellido, correo_electronico, telefono)
        print("\nEstudiante registrado exitosamente")
        
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nError inesperado: {e}")
    
    
def viewConsultarEstudiantes():
    print()
    print("#"*30)
    print("MODULO DE CONSULTA DE ESTUDIANTES")
    print("#"*30)
    
    try:
        estudiantes = controller_estudiantes.consultarEstudiantesController()
                
        print("\nLISTA DE ESTUDIANTES REGISTRADOS:")
        for estudiante in estudiantes:
            print(dedent(f"""
            ID: {estudiante.id_estudiante}  
            Nombre: {estudiante.nombre}
            Apellido: {estudiante.apellido} 
            Correo Electronico: {estudiante.correo_electronico}
            Telefono: {estudiante.telefono}"""))
                
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nError inesperado: {e}")
                
        
def viewConsultarEstudiante():
    print()
    print("#"*30)
    print("MODULO DE CONSULTA DE UN ESTUDIANTE")
    print("#"*30)
    try:
        id_estudiante = int(input("\nPor favor ingrese el id del estudiante a consultar: ").strip())
        
        if id_estudiante <= 0:
            raise ValueError("El id debe ser un numero entero positivo")
        
        estudiante = controller_estudiantes.consultarEstudianteController(id_estudiante)
        
        print("\nESTUDIANTE CONSULTADO:")                
        print(dedent(f"""
        ID: {estudiante.id_estudiante}  
        Nombre: {estudiante.nombre}
        Apellido: {estudiante.apellido} 
        Correo Electronico: {estudiante.correo_electronico}
        Telefono: {estudiante.telefono}"""))
            
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nError inesperado: {e}")        
    
    
def viewActualizarEstudiante():
    print()
    print("#"*30)
    print("MODULO DE ACTUALIZACIÓN DE UN ESTUDIANTE")
    print("#"*30)
    
    try:
        id_estudiante = int(input("\nPor favor ingrese el id del estudiante a actualizar: ").strip())
        
        if id_estudiante <= 0:
            raise ValueError("El id debe ser un numero entero positivo")
        
        estudiante_a_actualizar = controller_estudiantes.consultarEstudianteController(id_estudiante)
        
        nombre = input("\nPor favor ingrese el nombre del estudiante: ").strip()
        if not nombre:
            nombre = estudiante_a_actualizar.nombre
        
        apellido = input("Por favor ingrese el apellido del estudiante: ").strip()
        if not apellido:
            apellido = estudiante_a_actualizar.apellido 
            
        correo_electronico = input("Por favor ingrese el correo electronico del estudiante: ").strip()
        if not correo_electronico:
            correo_electronico = estudiante_a_actualizar.correo_electronico
        
        telefono = input("Por favor ingrese el numero de telefono del estudiante: ").strip()
        if not telefono:
            telefono = estudiante_a_actualizar.telefono 
        
        controller_estudiantes.actualizarEstudianteController(id_estudiante, nombre, apellido, correo_electronico, telefono)
        print("\nEstudiante actualizado exitosamente")
        
    except ValueError as e:
        print(f"\nError: {e}")
        
    except Exception as e:
        print(f"\nError inesperado: {e}")
                
    
def viewEliminarEstudiante():
    print()
    print("#"*30)
    print("MODULO DE ELIMINACIÓN DE UN ESTUDIANTE")
    print("#"*30)
    
    try:
        id_estudiante = int(input("\nPor favor ingrese el id del estudiante a eliminar: ").strip())
        
        if id_estudiante <= 0:
            raise ValueError("El id debe ser un numero entero positivo")
        
        eliminado = controller_estudiantes.eliminarEstudianteController(id_estudiante)
        if eliminado:
            print(f"\nEstudiante con ID {id_estudiante} eliminado exitosamente")
              
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nError inesperado: {e}")


def menuEstudiantesView():
    while True:
        print()
        print("#"*30)
        print("MODULO DE GESTION DE ESTUDIANTES")
        print("#"*30)
        print(dedent("""
        1. Registrar un Estudiante
        2. Consultar Estudiantes
        3. Consultar un Estudiante
        4. Actualizar un Estudiante
        5. Eliminar un Estudiante
        6. Salir
        """))
        
        try:
            opcion = int(input("Ingrese una opcion: ").strip())
            
            if opcion <= 0:
                raise ValueError("La opcion debe ser un numero entero positivo.")
            
            if opcion == 1:
                viewRegistrarEstudiante()
                
            elif opcion == 2:
                viewConsultarEstudiantes()
                
            elif opcion == 3:
                viewConsultarEstudiante()
                
            elif opcion == 4:
                viewActualizarEstudiante()
                
            elif opcion == 5:
                viewEliminarEstudiante()
                
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