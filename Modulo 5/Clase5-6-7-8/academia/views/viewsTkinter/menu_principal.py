import customtkinter as ctk
from views.viewsTkinter.view_estudiantes.menu_estudiantes import MenuEstudiantes

# Crear la clase principal de la ventana la cual se encargara de recibir las demas ventanas

class MenuPrincipal:
    def __init__(self, tema_actual="System"):
        self.root = ctk.CTk()
        self.root.title("Menu Principal")
    
        #Configurar el tema de la ventana
        ctk.set_appearance_mode(tema_actual)
        
        #Obtener el ancho y el alto de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()
        
        #Asignar tamaño de la ventana
        ancho_ventana = int(ancho_pantalla * 0.2)
        alto_ventana = int(alto_pantalla * 0.45)        
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}")
        
        #Configuración de restricciones de la ventana
        self.root.resizable(False, False) 
        
        # Coordenadas centradas
        x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y = (alto_pantalla // 2) - (alto_ventana // 2)
        
        # Establecer geometria con posicion centrada
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
        
        #Creamos el titulo de la ventana
        self.titulo = ctk.CTkLabel(self.root, text="Menu Principal", font=("Arial", 16))
        self.titulo.pack(pady=10)

        #Crear 5 botones para acceder a las demas ventanas
        """
        self.btn_estudiantes = ctk.CTkButton(self.root, text="Estudiantes", command=self.mostrar_ventana_estudiantes)
        self.btn_estudiantes.pack(pady=10)
        
        self.btn_profesores = ctk.CTkButton(self.root, text="Profesores", command=self.mostrar_ventana_profesores)
        self.btn_profesores.pack(pady=10)
        
        self.btn_cursos = ctk.CTkButton(self.root, text="Cursos", command=self.mostrar_ventana_cursos)
        self.btn_cursos.pack(pady=10)        
        
        self.btn_horarios = ctk.CTkButton(self.root, text="Horarios", command=self.mostrar_ventana_horarios)
        self.btn_horarios.pack(pady=10)
        
        self.btn_matriculas = ctk.CTkButton(self.root, text="Matriculas", command=self.mostrar_ventana_matriculas)
        self.btn_matriculas.pack(pady=10)
        """
        
        #Crear 5 botones para acceder a las demas ventanas de forma mas optimizada
        
        botones = [
            ("Estudiantes", self.mostrar_ventana_estudiantes),
            ("Profesores", self.mostrar_ventana_profesores),
            ("Cursos", self.mostrar_ventana_cursos),
            ("Horarios", self.mostrar_ventana_horarios),
            ("Matriculas", self.mostrar_ventana_matriculas)
        ]
        
        for i, (texto, comando) in enumerate(botones):
            boton = ctk.CTkButton(self.root, text=texto, command=comando)
            boton.pack(pady=10)
        
        #Boton para cambiar el tema de la ventana
        self.tema_actual = "System"
        self.btn_cambiar_tema = ctk.CTkButton(self.root, text="Cambiar Tema", command=self.cambiar_tema)
        self.btn_cambiar_tema.pack(pady=10)
        
    def mostrar_ventana_estudiantes(self):
        self.root.destroy()
        menu_estudiantes = MenuEstudiantes(self.tema_actual)
        menu_estudiantes.root.mainloop()
    
    def mostrar_ventana_profesores(self):
        pass
    
    def mostrar_ventana_cursos(self):
        pass
    
    def mostrar_ventana_horarios(self):
        pass
    
    def mostrar_ventana_matriculas(self):
        pass
    
    
    def cambiar_tema(self):
        if self.tema_actual == "Light":
            ctk.set_appearance_mode("Dark")
            self.tema_actual = "Dark"
        else:
            ctk.set_appearance_mode("Light")
            self.tema_actual = "Light"
        
        