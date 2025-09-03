class Libro:
    def __init__(self, titulo, autor) -> None:
        self.titulo = titulo
        self.autor = autor
    
    def description(self):
        return f"""Libro: {self.titulo}
        Autor: {self.autor}"""
    
    def __str__(self):
        return f"""Libro: {self.titulo}
        Autor: {self.autor}"""
    
class LibroDigital(Libro):
    def __init__(self, titulo, autor, formato) -> None:
        super().__init__(titulo, autor)
        self.formato = formato
        
        
    def description(self):
        return f"""Libro: {self.titulo}
        Autor: {self.autor}
        Fomato: {self.formato}"""
    
    def __str__(self):
        return f"""Libro: {self.titulo}
        Autor: {self.autor}
        Fomato: {self.formato}"""
            

libro1 = Libro("El poder del Ahora", "Eckhart Tolle")
libroDigital1 = LibroDigital("Habitos Atomicos", "James Clear", "PDF")

print(libro1.__str__())
print(libroDigital1.description())