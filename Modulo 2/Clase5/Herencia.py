import textwrap


class Vehiculo:
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def descripcion(self):
        return textwrap.dedent(f"""
        Marca: {self.marca}
        Modelo: {self.modelo}
        """)

class Auto(Vehiculo):
    
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def descripcion(self):
        return textwrap.dedent(f"""
        Estos son los datos del Auto:
        Marca: {self.marca}
        Modelo: {self.modelo}
        Número de puertas: {self.puertas}
        """)
        
auto1 = Auto("Toyota", "Corolla", 4)
print(auto1.descripcion())

auto2 = Auto("Chevrolet", "Captiva", 4)
print(auto2.descripcion())