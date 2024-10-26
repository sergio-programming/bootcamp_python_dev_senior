nombre = input("Por favor ingrese su nombre: ")
edad = int(input("Por favor ingrese su edad: "))

if edad >= 18:
    print(f"Estimado usuario {nombre} has aplicado para iniciar el proceso")
else:
    print(f"Estimado usuario {nombre} no has aplicado para iniciar el proceso")