def dividir(a, b):
    try:
        division = a / b
    except ZeroDivisionError:
        return "No es posible hacer una division entre cero"
    else:
        return f"{a} ÷ {b} = {division}"

while True:
    try:
        num1 = int(input("Por favor ingrese el primer número: "))
        num2 = int(input("Por favor ingrese el segundo número: "))
    except ValueError:
        print("Debe ingresar dos valores númericos para hacer una división")
        input("Presione <Enter> para continuar")
    else:
        break
    
print(dividir(num1, num2))

def divisionValidada():
    while True:
        try:
            num1 = int(input("Por favor ingrese el primer número: "))
            num2 = int(input("Por favor ingrese el segundo número: "))
            division = num1 / num2
        except ZeroDivisionError:
            print("No es posible hacer una division entre cero")
        except ValueError:
            print("Debe ingresar dos valores númericos para hacer una división")
        else:
            print(f"{num1} ÷ {num2} = {division}") 
            break
    
divisionValidada()
    
