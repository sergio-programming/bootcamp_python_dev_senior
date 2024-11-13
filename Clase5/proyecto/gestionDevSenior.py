#Declaracion de listas
estudiantes = []
docentes = []
cursos = ["Java", "Python"]
horarios = []

#Funcion para matricular
def matricularEstudiantes():
    print()
    print("#"*30)
    print("MODULO DE REGISTRO DE ESTUDIANTES")
    print("#"*30)
    nroEstudiantes = int(input("¿Cuantos estudiantes desea matricular?: "))
    for j in range(nroEstudiantes):
        nombre = input(f"\nPor favor ingrese el nombre del estudiante #{j+1} a matricular: ")
        print("Seleccione un curso a matricular")
        for i, curso in enumerate(cursos):
            print(f"{i+1}: {cursos[i]}")
        
        while True:
            cursoSeleccionado = int(input("Ingrese el curso a matricular: "))
            if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
                curso = cursos[cursoSeleccionado-1]
                break
            else:
                print("\nEl curso ingresado no esta dentro de la lista de cursos. Por favor intente de nuevo")
                input("Presione <Enter> para continuar")
                
        registroEstudiante = {
            "nombre": nombre,
            "curso": curso            
        }
        estudiantes.append(registroEstudiante)    
        print(f"""\nRegistro de estudiante exitoso
Nombre de estudiante: {nombre}
Curso matriculado: {curso}""")    
        
#Funcion para registrar docentes
def registrarDocente():
    print()
    print("#"*30)
    print("MODULO DE REGISTRO DE DOCENTES")
    print("#"*30)
    nroDocentes = int(input("¿Cuantos docentes desea matricular?: "))
    for j in range(nroDocentes):
        nombre = input(f"\nPor favor ingrese el nombre del docente #{j+1} a registrar: ")
        print("Seleccione un curso a asignar")
        for i, curso in enumerate(cursos):
            print(f"{i+1}: {cursos[i]}")
        
        while True:
            cursoSeleccionado = int(input("Ingrese el curso a asignar: "))
            if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
                curso = cursos[cursoSeleccionado-1]
                break
            else:
                print("\nEl curso ingresado no esta dentro de la lista de cursos. Por favor intente de nuevo")
                input("Presione <Enter> para continuar")
                
        registroDocente = {
            "nombre": nombre,
            "curso": curso            
        }
        docentes.append(registroDocente)    
        print(f"""\nRegistro de docente exitoso
Nombre del docente: {nombre}
Curso asignado: {curso}""") 

#Funcion para asignar horarios       
def asignarHorario():
    print()
    print("#"*30)
    print("MODULO DE REGISTRO HORARIOS")
    print("#"*30)
    print("Seleccione un curso a asignar")
    for i, curso in enumerate(cursos):
        print(f"{i+1}: {cursos[i]}")
        
        while True:
            cursoSeleccionado = int(input("Ingrese el curso a asignar: "))
            if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
                curso = cursos[cursoSeleccionado-1]
                dias = input("Por favor ingrese los dias de clases (ej: Martes y jueves): ")
                hora = input("Por favor ingrese el horario de las clases (ej: 6 pm): ")
                horario = {
                    "curso": curso,
                    "dias": dias,
                    "hora": hora
                }        
                break
            else:
                print("El curso ingresado no esta dentro de la lista de cursos. Por favor intente de nuevo")
                input("Presione <Enter> para continuar")
        horarios.append(horario)

#Funcion para mostrar los estudiantes matriculados        
def mostrarEstudiantes():
    if estudiantes:
        print("\nLista de estudiantes matriculados")
        for estudiante in estudiantes:
            print(f"""\nNombre del estudiante: {estudiante['nombre']}
Curso matriculado: {estudiante['curso']}""")
    else:
        print("No hay registros de estudiantes matriculados.")

#Funcion para mostrar los docentes registrados        
def mostrarDocentes():
    if docentes:
        print("\nLista de docentes registrados")
        for docente in docentes:
            print(f"""\nNombre del docente: {docente['nombre']}
Curso asignado: {docente['curso']}""")
    else:
        print("No hay registros de docentes matriculados.")

#Funcion para mostrar los horarios       
def mostrarHorarios():
    if horarios:
        print("\nEstos son los horarios de los cursos:")
        for horario in horarios:
            print(f"""\nCurso: {horario['curso']}
Dias: {horario['dias']}
Hora:"{horario['hora']}""")
    else:
        print("No hay registros de horarios.")
            
while True:
    print()
    print("#"*30)
    print("BIENVENIDO A LA PLATAFORMA DE DEV SENIOR")
    print("#"*30)
    print("""1. Matricular estudiantes.
2. Registrar docentes.
3. Mostrar registros de estudiantes.
4. Mostrar registros de docentes.
5. Mostrar horarios.
6. Salir del programa.""")
    
    opcion = int(input("Por favor digite una opcion: "))
    
    if opcion == 1:
        matricularEstudiantes()
        
    elif opcion == 2:
        registrarDocente()
        
    elif opcion == 3:
        mostrarEstudiantes()
        
    elif opcion == 4:
        mostrarDocentes()
        
    elif opcion == 5:
        mostrarHorarios()
    
    elif opcion == 6:
        print("\nGracias por usar nuestra plataforma. HASTA PRONTO!!!")
        input("Ingrese <Enter> para continuar")
        break
    
    else:
        print("\nLa opcion ingresada no es valida. Por favor intente de nuevo.")
        input("Presione <Enter> para continuar")
        
    