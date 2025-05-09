import customtkinter as ctk
import re
from controllers.estudiantes_controller import EstudianteController

class RegistrarEstudiante:
    def __init__(self, tema_actual="System"):    
        self.root = ctk.CTk()
        self.root.title("Registrar Estudiante")
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
        self.titulo = ctk.CTkLabel(self.root, text="Registrar Estudiante", font=("Arial", 16))
        self.titulo.pack(pady=10)
        
        # Frame para campos de entrada
        self.frame_entrada = ctk.CTkFrame(self.root)
        self.frame_entrada.pack(pady=10)

        # Campo de nombre
        self.label_nombre = ctk.CTkLabel(self.frame_entrada, text="Nombre:")
        self.label_nombre.grid(row=0, column=0, padx=5, pady=5)
        self.entry_nombre = ctk.CTkEntry(self.frame_entrada)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        # Campo de apellido
        self.label_apellido = ctk.CTkLabel(self.frame_entrada, text="Apellido:")
        self.label_apellido.grid(row=1, column=0, padx=5, pady=5)
        self.entry_apellido = ctk.CTkEntry(self.frame_entrada)
        self.entry_apellido.grid(row=1, column=1, padx=5, pady=5)

        # Campo de correo
        self.label_correo = ctk.CTkLabel(self.frame_entrada, text="Correo:")
        self.label_correo.grid(row=2, column=0, padx=5, pady=5)
        self.entry_correo = ctk.CTkEntry(self.frame_entrada)
        self.entry_correo.grid(row=2, column=1, padx=5, pady=5)

        # Campo de teléfono
        self.label_telefono = ctk.CTkLabel(self.frame_entrada, text="Teléfono:")
        self.label_telefono.grid(row=3, column=0, padx=5, pady=5)
        self.entry_telefono = ctk.CTkEntry(self.frame_entrada)
        self.entry_telefono.grid(row=3, column=1, padx=5, pady=5)

        # Frame para los botones
        self.frame_botones = ctk.CTkFrame(self.root)
        self.frame_botones.pack(pady=10)

        # Botón Registrar
        self.btn_registrar = ctk.CTkButton(self.frame_botones, text="Registrar", command=self.registrar_estudiante)
        self.btn_registrar.pack(pady=5)

        # Botón Regresar
        self.btn_regresar = ctk.CTkButton(self.frame_botones, text="Regresar", command=self.regresar_menu_estudiantes)
        self.btn_regresar.pack(pady=5)
        
    def regresar_menu_estudiantes(self):
        self.root.destroy()
        from views.viewsTkinter.view_estudiantes.menu_estudiantes import MenuEstudiantes
        menu_estudiantes = MenuEstudiantes(self.tema_actual)
        menu_estudiantes.root.mainloop()
        
    def registrar_estudiante(self):
        from views.viewsTkinter.view_estudiantes.menu_estudiantes import MenuEstudiantes
        nombre = self.entry_nombre.get().strip()
        apellido = self.entry_apellido.get().strip()
        correo = self.entry_correo.get().strip()
        telefono = self.entry_telefono.get().strip()
        
        if not self.validar_campos():
            return
        
        try:
            self.estudiante_controller.registrarEstudianteController(nombre, apellido, correo, telefono)
            self.limpiar_campos()
            self.notificacion(mensaje="Estudiante registrado exitosamente")
            
        except Exception as e:
            self.limpiar_campos()
            self.notificacion(mensaje="Error al registrar estudiante")
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
        
    def limpiar_campos(self):
        self.entry_nombre.delete(0, ctk.END)
        self.entry_apellido.delete(0, ctk.END)
        self.entry_correo.delete(0, ctk.END)
        self.entry_telefono.delete(0, ctk.END)
        
    def validar_campos(self):
        nombre = self.entry_nombre.get().strip()
        apellido = self.entry_apellido.get().strip()
        correo = self.entry_correo.get().strip()
        telefono = self.entry_telefono.get().strip()

        if not nombre:
            self.notificacion(mensaje="El campo de nombre es obligatorio")
            return False
        if not apellido:
            self.notificacion(mensaje="El campo de apellido es obligatorio")
            return False
        if not correo or not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", correo):
            self.notificacion(mensaje="Ingrese un correo válido")
            return False
        if not telefono or not telefono.isdigit():
            self.notificacion(mensaje="El teléfono debe contener solo números")
            return False

        return True
    
    def limpiar_campos(self):
        self.entry_nombre.delete(0, ctk.END)
        self.entry_apellido.delete(0, ctk.END)
        self.entry_correo.delete(0, ctk.END)
        self.entry_telefono.delete(0, ctk.END)