import random
import time

def sensorClima():
    while True:
        temperatura = round(random.uniform(10.0, 35.0), 2)
        yield f"Temperatura Actual: {temperatura}°C"
        input("Presione <Enter> para continuar")
        
for lectura in sensorClima():
    print(lectura)