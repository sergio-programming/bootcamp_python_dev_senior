print("#"*30)
print("BIENVENIDO A LA CALCULADORA")
print("#"*30)

print("\nIngrese dos numeros para hacer las operaciones matemáticas básicas.\n")

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

suma = num1 + num2
resta = num1 - num2
multp = num1 * num2
division = num1 / num2

print(f"\n{num1} + {num2} = {suma}")
print(f"{num1} - {num2} = {resta}")
print(f"{num1} X {num2} = {multp}")
print(f"{num1} ÷ {num2} = {division}")
