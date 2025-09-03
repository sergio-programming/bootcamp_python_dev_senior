def compararTresNumeros():
    while True:
        try:
            num1 = int(input("Por favor ingrese el primer número: "))
            num2 = int(input("Por favor ingrese el segundo número: "))
            num3 = int(input("Por favor ingrese el tercer número: "))
        except ValueError:
            print("Debe ingresar valores númericos para realizar la comparación")
            input("Presione <Enter> para intentar nuevamente.")
            continue
        else:
            if num1 > num2 and num2 > num3:
                print(f"Número mayor: {num1} // Número intermedio: {num2} // Número menor: {num3}")
            elif num1 > num3 and num3 > num2:
                print(f"Número mayor: {num1} // Número intermedio: {num3} // Número menor: {num2}")
            elif num2 > num1 and num1 > num3:
                print(f"Número mayor: {num2} // Número intermedio: {num1} // Número menor: {num3}")
            elif num2 > num3 and num3 > num1:
                print(f"Número mayor: {num2} // Número intermedio: {num3} // Número menor: {num1}")
            elif num3 > num1 and num1 > num2:
                print(f"Número mayor: {num3} // Número intermedio: {num1} // Número menor: {num2}")
            elif num3 > num2 and num2 > num1:
                print(f"Número mayor: {num3} // Número intermedio: {num2} // Número menor: {num1}")
            elif num1 == num2 and num1 != num3:
                print(f"Números iguales: {num1} = {num2} // Número diferente: {num3}")
            elif num1 == num3 and num1 != num2:
                print(f"Números iguales: {num1} = {num3} // Número diferente: {num2}")
            elif num2 == num3 and num2 != num1:
                print(f"Números iguales: {num2} = {num3} // Número diferente: {num1}")
            else:
                print(f"Los tres números son iguales: {num1} = {num2} = {num3}")
                input("Presione <Enter> para continuar")
        finally:
            print("Comparación realizada de manera exitosa")  
              
        while True:
            otra_vez = input("¿Desea realizar otra comparación? (si/no): ").strip().lower()
            if otra_vez in  ["si", "no"]:
                break
            print("Por favor ingrese una respuesta valida: 'si' o 'no'")
            
        if otra_vez == "no":
            
            print("Gracias por usar el programa. Hasta pronto!!")
            break


compararTresNumeros()