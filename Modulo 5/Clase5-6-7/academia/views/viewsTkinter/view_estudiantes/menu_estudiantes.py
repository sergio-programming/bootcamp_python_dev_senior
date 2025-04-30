import customtkinter as ctk
from views.viewsTkinter.view_estudiantes.consultar_estudiantes import ConsultarEstudiantes
from views.viewsTkinter.view_estudiantes.registrar_estudiante import RegistrarEstudiante

class MenuEstudiantes:
    def __init__(self, tema_actual="System"):
        self.root = ctk.CTk()
        self.root.title("Menu Estudiantes")
        
        #Configurar el tema de la ventana
        ctk.set_appearance_mode(tema_actual)
        
        #Configurar cierre de la ventana
        self.root.protocol("WM_DELETE_WINDOW", self.regresar_menu_principal)
        
        #Obtener el ancho y el alto de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()
        
        #Asignar tamaño de la ventana
        ancho_ventana = int(ancho_pantalla * 0.3)
        alto_ventana = int(alto_pantalla * 0.4)
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}")
        
        # Coordenadas centradas
        x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y = (alto_pantalla // 2) - (alto_ventana // 2)
        
        #Establecer geometria con posicion centrada
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")        
        
        #Configuración de restricciones de la ventana
        self.root.resizable(False, False)
        
        #Titulo de la ventana
        self.titulo = ctk.CTkLabel(self.root, text="Menu Estudiantes", font=("Arial", 16))
        self.titulo.pack(pady=10)
        
        #Boton para cambiar el tema de la ventana
        self.tema_actual = "System"
        self.btn_cambiar_tema = ctk.CTkButton(self.root, text="Cambiar Tema", command=self.cambiar_tema)
        self.btn_cambiar_tema.pack(pady=10)
        
        #Boton para mostrar estudiantes en una ventana emergente
        self.btn_consultar_estudiantes = ctk.CTkButton(self.root, text="Consultar Estudiantes", command=self.consultar_estudiantes)
        self.btn_consultar_estudiantes.pack(pady=10)
        
        #Boton para Registrar estudiante
        self.btn_crear_estudiante = ctk.CTkButton(self.root, text="Registrar Estudiante", command=self.registrar_estudiante)
        self.btn_crear_estudiante.pack(pady=10)    
        
        #Crear boton para regresar al menu principal
        self.boton_regresar = ctk.CTkButton(self.root, text="Regresar", command=self.regresar_menu_principal)
        self.boton_regresar.pack(pady=10)
        
        
    def regresar_menu_principal(self):
        from ..menu_principal import MenuPrincipal
        self.root.destroy()
        menu_principal = MenuPrincipal(self.tema_actual)
        menu_principal.root.mainloop()

    def cambiar_tema(self):
        if self.tema_actual == "Light":
            ctk.set_appearance_mode("Dark")
            self.tema_actual = "Dark"
        else:
            ctk.set_appearance_mode("Light")
            self.tema_actual = "Light"
            
    def consultar_estudiantes(self):
        from views.viewsTkinter.view_estudiantes.consultar_estudiantes import ConsultarEstudiantes
        consultar_estudiantes = ConsultarEstudiantes(self.tema_actual)
        consultar_estudiantes.root.mainloop() 
    
    def registrar_estudiante(self):
        from views.viewsTkinter.view_estudiantes.registrar_estudiante import RegistrarEstudiante
        crear_estudiante = RegistrarEstudiante(self.tema_actual)
        crear_estudiante.root.mainloop()