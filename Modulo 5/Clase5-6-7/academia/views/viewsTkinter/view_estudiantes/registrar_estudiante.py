import customtkinter as ctk
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
        self.btn_regresar = ctk.CTkButton(self.frame_botones, text="Regresar", command=self.regresar_menu_principal)
        self.btn_regresar.pack(pady=5)

    def regresar_menu_principal(self):
        from ..menu_principal import MenuPrincipal
        self.root.destroy()
        menu_principal = MenuPrincipal(self.tema_actual)
        menu_principal.root.mainloop()
        
    def registrar_estudiante(self):
        from ..menu_principal import MenuPrincipal
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        correo = self.entry_correo.get()
        telefono = self.entry_telefono.get()
        
        try:
            self.estudiante_controller.registrarEstudianteController(nombre, apellido, correo, telefono)
            self.root.destroy()
            menu_principal = MenuPrincipal(self.tema_actual)
            menu_principal.root.mainloop()
        except Exception as e:
            print(f"Error inesperado: {e}")