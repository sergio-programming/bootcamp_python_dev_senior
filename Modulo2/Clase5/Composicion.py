class Motor:    
    def __init__(self):
        pass
    
    def iniciar(self):
        pass
    
    
class MotorCombustion(Motor):    
    def __init__(self):
        pass
    
    def iniciar(self):
        print("Motor de combustión encendido")    
    
class MotorElectrico(Motor):    
    def __init__(self):
        pass
    
    def iniciar(self):
        print("Motor de electrico encendido")
        
class Vehiculo:
    def __init__(self, motor):
        self.motor = motor
    
    def encender(self):
        print("Encendiendo el vehiculo")
        self.motor.iniciar()
    
motor_combustion = MotorCombustion()
motor_electrico = MotorElectrico()
    
auto_combustion = Vehiculo(motor_combustion)
auto_electrico = Vehiculo(motor_electrico)

auto_combustion.encender()
auto_electrico.encender()

