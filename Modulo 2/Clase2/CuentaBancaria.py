class CuentaBancaria:
    def __init__(self, nombreUsuario, dni, saldo, clave):
        self.nombreUsuario = nombreUsuario
        self.dni = dni
        self._saldo = saldo
        self.__clave = clave
        pass
    
    def depositar(self, montoDeposito):
        if montoDeposito <= 10000:
            return f"""No ingresaste la cantidad minima para depositar ($10.000)
Saldo Actual: ${self._saldo} pesos"""
            
    
        else:
            self._saldo += montoDeposito
            return f"""Acabas de depositar ${montoDeposito} pesos en la cuenta
Saldo Actual: ${self._saldo} pesos"""
            

    def retirar(self, montoRetiro):
        if montoRetiro > self._saldo:
            return f"""No es posible retirar una cantidad mayor al saldo
Saldo Actual: ${self._saldo} pesos"""
            
        
        else:
            self._saldo -= montoRetiro
            return f"""Acabas de retirar ${montoRetiro} de la cuenta
Saldo Actual: ${self._saldo} pesos"""
            
    
    def modificarClave(self, nuevaClave):
        self.__clave = nuevaClave
        print("Clave modificada exitosamente")
    
    
cuenta1 = CuentaBancaria("Sergio Pedraza", "1032421747", 0, "881003")

print(f"Nombre de Usuario: {cuenta1.nombreUsuario}")
print(f"DNI: {cuenta1.dni}")
print(f"Saldo: ${cuenta1._saldo}")
print()

print(cuenta1.depositar(150000))
print(cuenta1.depositar(5000))

print(cuenta1.retirar(100000))
print(cuenta1.retirar(200000))