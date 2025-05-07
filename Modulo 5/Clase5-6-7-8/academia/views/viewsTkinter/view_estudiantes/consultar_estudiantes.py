import customtkinter as ctk
import tkinter.ttk as ttk
from controllers.estudiantes_controller import EstudianteController

class ConsultarEstudiantes:
    def __init__(self, tema_actual="System"):
        self.root = ctk.CTk()    
        self.root.title("Consultar Estudiantes")
        self.estudiante_controller = EstudianteController()
        
        #Configurar el tema de la ventana
        ctk.set_appearance_mode(tema_actual)
        
        #Obtener el ancho y el alto de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()
        
        #Asignar tamaño de la ventana
        ancho_ventana = int(ancho_pantalla * 0.4)
        alto_ventana = int(alto_pantalla * 0.6)
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}")
        
        #Configuración de restricciones de la ventana
        self.root.resizable(False, False)
        
        #Titulo de la ventana
        self.titulo = ctk.CTkLabel(self.root, text="Consultar Estudiantes", font=("Arial", 16))
        self.titulo.pack(pady=10)
        
        
        #Crear un frame para la tabla
        self.frame_tabla = ctk.CTkFrame(self.root)
        self.frame_tabla.pack(pady=10)
        
        #Crear Treeview
        self.tabla = ttk.Treeview(self.frame_tabla, columns=("ID", "Nombre", "Apellido", "Correo_electronico", "Telefono"), show="headings")
        
        #Definir encabezados
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Apellido", text="Apellido")
        self.tabla.heading("Correo_electronico", text="Correo Electronico")
        self.tabla.heading("Telefono", text="Telefono")
        
        #Establecer ancho de las columnas
        self.tabla.column("ID", width=50)
        self.tabla.column("Nombre", width=100)
        self.tabla.column("Apellido", width=100)
        self.tabla.column("Correo_electronico", width=150)
        self.tabla.column("Telefono", width=100)
        
        self.tabla.pack(expand=True, fill="both")
        
        #Cargar los datos de la tabla
        self.cargar_datos_tabla()
        
    def cargar_datos_tabla(self):
        estudiantes = self.estudiante_controller.consultarEstudiantesController()
        for estudiante in estudiantes:
            self.tabla.insert("", "end", values=(
                estudiante.id_estudiante,
                estudiante.nombre,
                estudiante.apellido,
                estudiante.correo_electronico,
                estudiante.telefono
            ))
        
        