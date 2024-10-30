nombre = input("Por favor ingrese el nombre: ")
edad = int(input("Por favor ingrese la edad: "))

if edad >= 0 and edad < 6:
    print(f"Hola {nombre}, estas en la primera infancia")
elif edad >= 6 and  edad < 12:
    print(f"Hola {nombre}, estas en la infancia")
elif edad >= 12 and edad < 18:
    print(f"Hola {nombre}, estas en la adolescencia")
elif edad >= 18 and edad < 27:
    print(f"Hola {nombre}, estas en la juventud")
elif edad >= 27 and edad < 50:
    print(f"Hola {nombre}, estas en la adultez")
elif edad >=50 and edad < 65:
    print(f"Hola {nombre}, eres un adulto mayor")
elif edad >= 65 and edad <= 120:
    print(f"Hola {nombre}, estas en la vejez")
elif edad < 0:
    print(f"La edad no puede ser negativa")
else:
    print(f"No es posible que tengas esa edad")
    
    