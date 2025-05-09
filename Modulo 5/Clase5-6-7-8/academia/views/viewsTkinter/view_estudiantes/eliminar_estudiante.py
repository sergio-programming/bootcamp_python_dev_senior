import customtkinter as ctk
from controllers.estudiantes_controller import EstudianteController

class EliminarEstudiante:
    def __init__(self, tema_actual="System"):
        self.root = ctk.CTk()
        self.root.title("Eliminar Estudiante")
        self.estudiante_controller = EstudianteController()
        self.tema_actual = tema_actual
        
        # Configurar el tema de la ventana  
        ctk.set_appearance_mode(tema_actual)
        
        # Obtener el ancho y el alto de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()
        
        # Asignar tamaño de la ventana
        ancho_ventana = int(ancho_pantalla * 0.3)
        alto_ventana = int(alto_pantalla * 0.45)
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}")
        
        # Configuración de restricciones de la ventana
        self.root.resizable(False, False)
        
        # Configurar cierre de la ventana
        self.root.protocol("WM_DELETE_WINDOW", self.regresar_menu_estudiantes)
        
        # Título de la ventana
        self.titulo = ctk.CTkLabel(self.root, text="Eliminar Estudiante", font=("Arial", 16))
        self.titulo.pack(pady=10)
        
        # Frame para el campo de entrada
        self.frame_entrada = ctk.CTkFrame(self.root)
        self.frame_entrada.pack(pady=10)
        
        # Campo de entrada para el ID del estudiante
        self.id_label = ctk.CTkLabel(self.frame_entrada, text="ID del Estudiante:")
        self.id_label.pack(pady=5)
        self.id_entry = ctk.CTkEntry(self.frame_entrada)
        self.id_entry.pack(pady=5)
        
        # Frame para los botones
        self.frame_botones = ctk.CTkFrame(self.root)
        self.frame_botones.pack(pady=10)
        
        # Botón para eliminar el estudiante
        self.eliminar_button = ctk.CTkButton(self.frame_botones, text="Eliminar Estudiante", command=self.eliminar_estudiante)
        self.eliminar_button.pack(pady=10)
        
        # Botón Regresar
        self.btn_regresar = ctk.CTkButton(self.frame_botones, text="Regresar", command=self.regresar_menu_estudiantes)
        self.btn_regresar.pack(pady=10)
        
    
    def regresar_menu_estudiantes(self):
        self.root.destroy()
        from views.viewsTkinter.view_estudiantes.menu_estudiantes import MenuEstudiantes
        menu_estudiantes = MenuEstudiantes(self.tema_actual)
        menu_estudiantes.root.mainloop()

    def eliminar_estudiante(self):
        from views.viewsTkinter.view_estudiantes.menu_estudiantes import MenuEstudiantes        
        id = self.id_entry.get().strip()
        
        if not self.validar_campo():
            return
        
        try:
            self.estudiante_controller.eliminarEstudianteController(id)
            self.id_entry.delete(0, "end")
            self.notificacion(mensaje="Estudiante eliminado exitosamente")
                            
        except Exception as e:
            self.id_entry.delete(0, "end")
            self.notificacion(mensaje="Error al eliminar estudiante")
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