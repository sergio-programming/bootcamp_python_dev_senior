from textwrap import dedent
from views.estudiantes_view import menuEstudiantesView
from views.profesores_view import menuProfesoresView
from views.cursos_view import menuCursosView
from views.matriculas_view import menuMatriculasView
from views.horarios_view import menuHorariosView

def menu():
    while True:
        print()
        print("#"*30)
        print("BIENVENIDOS A LA PLATAFORMA DE GESTIÓN DE LA ACADEMIA")
        print("#"*30)
        print(dedent("""
        1. Gestión de Estudiantes.
        2. Gestión de Profesores.
        3. Gestión de Cursos.
        4. Gestión de Matriculas.
        5. Gestión de Horarios.
        6. Salir.
        """))
        
        try:
            opcion = int(input("Ingrese una opción: ").strip())
            
            if opcion <= 0:
                raise ValueError("La opcion debe ser un numero entero positivo.")
        
            if opcion == 1:
                menuEstudiantesView()
                
            elif opcion == 2:
                menuProfesoresView()
            
            elif opcion == 3:
                menuCursosView()
            
            elif opcion == 4:
                menuMatriculasView()
            
            elif opcion == 5:
                menuHorariosView()
            
            elif opcion == 6:
                print("Gracias por usar la plataforma de la academia. Hasta pronto!")
                break
            
            else:
                print("La opcion elegida no es valida. Por favor intente de nuevo.")
                input("Presione <Enter> para continuar")
                
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
        
        
            
            
            