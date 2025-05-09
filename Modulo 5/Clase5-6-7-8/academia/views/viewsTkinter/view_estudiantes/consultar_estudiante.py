import customtkinter as ctk
import tkinter.ttk as ttk
from controllers.estudiantes_controller import EstudianteController

class ConsultarEstudiante:
    def __init__(self, tema_actual="System"):
        self.root = ctk.CTk()
        self.root.title("Consultar un Estudiante")
        self.estudiante_controller = EstudianteController()
        self.tema_actual = tema_actual
        
        # Configurar el tema de la ventana  
        ctk.set_appearance_mode(tema_actual)
        
        # Obtener el ancho y el alto de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()
        
        # Asignar tamaño de la ventana
        ancho_ventana = int(ancho_pantalla * 0.4)
        alto_ventana = int(alto_pantalla * 0.45)
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}")
        
        # Configuración de restricciones de la ventana
        self.root.resizable(False, False)
        
        # Configurar cierre de la ventana
        self.root.protocol("WM_DELETE_WINDOW", self.regresar_menu_estudiantes)
        
        # Título de la ventana
        self.titulo = ctk.CTkLabel(self.root, text="Consultar Estudiante", font=("Arial", 16))
        self.titulo.pack(pady=10)
        
        #Crear un frame para la tabla
        self.frame_tabla = ctk.CTkFrame(self.root)
        self.frame_tabla.pack(pady=10)
        
        #Crear Treeview
        self.tabla = ttk.Treeview(self.frame_tabla, columns=("ID", "Nombre", "Apellido", "Correo_electronico", "Telefono"), show="headings", height=3)
        
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
        
        # Frame para el ID
        self.frame_id = ctk.CTkFrame(self.root)
        self.frame_id.pack(pady=10)
        
        # Etiqueta y entrada para el ID
        self.id_label = ctk.CTkLabel(self.frame_id, text="ID:")
        self.id_label.pack(side="left")
        self.id_entry = ctk.CTkEntry(self.frame_id)
        self.id_entry.pack(side="left")
        
        # Frame para los botones
        self.frame_botones = ctk.CTkFrame(self.root)
        self.frame_botones.pack(pady=10)
        
        # Botón para eliminar el estudiante
        self.eliminar_button = ctk.CTkButton(self.frame_botones, text="Consultar Estudiante", command=self.cargar_datos_tabla)
        self.eliminar_button.pack(pady=10)
        
        # Botón Regresar
        self.btn_regresar = ctk.CTkButton(self.frame_botones, text="Regresar", command=self.regresar_menu_estudiantes)
        self.btn_regresar.pack(pady=10)
        
    def cargar_datos_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        
        id = self.id_entry.get().strip()
        
        if not self.validar_campo():
            return
        
        try:
            estudiante = self.estudiante_controller.consultarEstudianteController(id)
            if estudiante:
                self.tabla.insert("", "end", values=(
                    estudiante.id_estudiante,
                    estudiante.nombre,
                    estudiante.apellido,
                    estudiante.correo_electronico,
                    estudiante.telefono
                ))
                self.id_entry.delete(0, "end")
            
        except Exception as e:
            self.id_entry.delete(0, "end")
            self.notificacion(mensaje="Error al consultar estudiante")
            print(f"Error inesperado: {e}")        
            
     
    def notificacion(self, mensaje):
        ventana_notificacion = ctk.CTk()
        ventana_notificacion.title("Notificación")
        ventana_notificacion.geometry("300x120")
        ventana_notificacion.resizable(False, False)
        label_notificacion = ctk.CTkLabel(ventana_notificacion, text=mensaje, font=("Arial", 12))
        label_notificacion.pack(pady=10)
        btn_aceptar = ctk.CTkButton(ventana_notificacion, text="Aceptar", command=ventana_notificacion.destroy)
        btn_aceptar.pack(pady=10)
        ventana_notificacion.mainloop()
        
    def validar_campo(self):
        id = self.id_entry.get().strip()
        
        if not id or not id.isdigit():
            self.notificacion(mensaje="El id debe ingresarse y contener solo números")
            return False
        return True
    
    def regresar_menu_estudiantes(self):
        self.root.destroy()
        from views.viewsTkinter.view_estudiantes.menu_estudiantes import MenuEstudiantes
        menu_estudiantes = MenuEstudiantes(self.tema_actual)
        menu_estudiantes.root.mainloop()