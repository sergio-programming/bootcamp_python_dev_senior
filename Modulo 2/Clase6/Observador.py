from abc import ABC, abstractmethod

class Sujeto:
    def __init__(self):
        self._observadores = []
        
    def agregarObservador(self, observador):
        self._observadores.append(observador)
        
    def quitarObservador(self, observador):
        self._observadores.remove(observador)
        
    def notificarObservador(self, mensaje):
        for observador in self._observadores:
            observador.actualizar(mensaje)

class Observador(ABC):
    
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def actualizar(self, mensaje):
        raise NotImplementedError("Subclases deben estar implementadas")
    

class ObservadorConcreto(Observador):
    def __init__(self, nombre):
        self._nombre = nombre
        
    def actualizar(self, mensaje):
        print(f"{self._nombre} recibió: {mensaje}") 
        
sujeto = Sujeto()

observador1 = ObservadorConcreto("Observador 1")       
observador2 = ObservadorConcreto("Observador 2")

sujeto.agregarObservador(observador1)       
sujeto.agregarObservador(observador2)       

sujeto.notificarObservador("Mensaje de adevertencia LPTx")