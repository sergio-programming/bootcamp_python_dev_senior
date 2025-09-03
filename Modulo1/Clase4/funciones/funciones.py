def suma(a, b):
    suma = a + b
    return f"{a} + {b} = {suma}"

def resta(a, b):
    resta = a - b
    return f"{a} - {b} = {resta}"

def multiplicacion(a, b):
    multp = a * b
    return f"{a} X {b} = {multp}"

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

print(suma(num1, num2))
print(resta(num1, num2))
print(multiplicacion(num1, num2))