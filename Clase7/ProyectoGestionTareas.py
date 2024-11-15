from datetime import datetime
import statistics

class Tarea:
    def __init__(self, nombre, fechaLimite, categoria, horasDedicadas):
        self.nombre = nombre
        self.fechaLimite = fechaLimite
        self.categoria = categoria
        self.horasDedicadas = horasDedicadas
        
    def ingresarTareas(listaTareas):
        nombre = input("Por favor ingrese el nombre de las tarea: ")
        fechaLimite_str = input("Por favor ingrese la fecha limite de la tarea: ")
        try:
            fechaLimite = datetime.striptime(fechaLimite_str, "%d,%m,%Y")
        except ValueError:
            print("La fecha ingresada no es valida. Por favor intente de nuevo.")
            return
        categoria = input("Ingrese la categoria de la tarea (Estudio, Personal, Trabajo): ")
        horasDedicadas_str = input("Ingrese las horas dedicadas separadas en comas: ")
        try:
            horasDedicadas = list(map(float, horasDedicadas_str.split(",")))
        except ValueError:
            print("Las horas ingresadas no esta en un formato valido. Por favor intente de nuevo.")
            return
        
        tarea = Tarea(nombre, fechaLimite, categoria, horasDedicadas)
        listaTareas.append(tarea)
        print("Tarea agregada exitosamente!")
        
    def visualizarTareas(listaTareas):
        if not listaTareas:
            print("No hay tareas registradas.")
            return
        
        for i, tarea in enumerate(listaTareas, start=1):
            print(f"""Tarea #{i}:
        Nombre de tarea: {tarea.nombre}
        Fecha limite: {tarea.fechaLimite.strftime('%d/%m/%Y')}
        Categoria: {tarea.categoria}
        Horas dedicadas: {tarea.horasDedicadas}""")
        
    def analizarHoras(listaTareas):
        if not listaTareas:
            print("No hay tareas registradas.")
            return
        
        for tarea in listaTareas:
            promedio = statistics.mean(tarea.horasDedicadas)
            maximo = max(tarea.horasDedicadas)
            minimo = min(tarea.horasDedicadas)
            print(f"""Analisis de horas de la tarea "{tarea.nombre}"
        Promedio de horas: {promedio}
        Maximo de horas: {maximo}
        Minimo de horas: {minimo}""")
        
    def generarInforme(listaTareas):
        if not listaTareas:
            print("No hay tareas registradas.")
            return
        
        with open("informe_tareas.txt", "w") as archivo:
            for tarea in listaTareas:
                archivo.write(f"Nombre: {tarea.nombre}\n")
                archivo.write(f"Fecha limite: {tarea.fechaLimite.strftime('%d/%m/%Y')}")
                archivo.write(f"Categoria: {tarea.categoria}\n")
                archivo.write(f"Horas dedicadas: {tarea.horasDedicadas}\n")
                archivo.write("\n")
        print("Informe generado como 'informe_tareas.txt")
        
        
listaTareas = []
while True:
    print()
    print("#"*30)
    print("PROGRAMA DE GESTION DE TAREAS")
    print("#"*30)
    print("""1. Gestion de Tareas.
2. Visualizacion de Tareas.
3. Analisis de horas dedicadas.
4. Generacion de informe.
5. Salir del programa.""")
    
    while True:
        try:
            opcion = int(input("\nPor favor digite su opción:"))
        except ValueError:
            print("El dato ingresado no es valido. Por favor ingrese un número.")
            input("Presione <Enter> para continuar")    
        else:
            break
        
    if opcion == 1:
        Tarea.ingresarTareas(listaTareas)
    
    elif opcion == 2:
        Tarea.visualizarTareas(listaTareas)
    
    elif opcion == 3:
        Tarea.analizarHoras(listaTareas)
    
    elif opcion == 4:
        Tarea.generarInforme(listaTareas)
    
    elif opcion == 5:
        print("Gracias por usar nuestro software, nos vemos pronto!!!")
        input("Presione <Enter> para continuar")
        break
    
    else:
        print("La opción ingresada no es valida. Por favor intente de nuevo.")
        input("Presione <Enter> para continuar")