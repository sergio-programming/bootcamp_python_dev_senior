num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
base = int(input("Ingrese un numero para elevarlo al cuadrado: "))

suma = num1 + num2
resta = num1 - num2
multp = num1 * num2
division = num1 / num2
residuo = num1 % num2
potencia = base**2

print(f"{num1} + {num2} = {suma}")
print(f"{num1} - {num2} = {resta}")
print(f"{num1} X {num2} = {multp}")
print(f"{num1} ÷ {num2} = {division}")
print(f"{num1} % {num2} = {residuo}")
print(f"{base}² = {potencia}")