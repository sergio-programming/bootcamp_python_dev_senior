#Variable para almacenar las ventas totales
ventasTotales = 0.0

#Listas para almacenar los productos
nombreArticulo = []
precioArticulo = []
cantidadArticulo = []

while True:
    print("#"*30)
    print("BIENVENIDOS A DROGAS LA ECONOMICA")
    print("#"*30)
    print("""1. Configuracion inicial de productos.
    2. Venta de productos.
    3. Mostrar inventario
    4. Mostrar ventas totales.
    5. Salir del programa.""")
    
    opcion = int(input("\nPor favor digite una opcion: "))
    
    if opcion == 1:
        print()
        print("#"*30)
        print("\nMODULO DE VENTAS")
        print("#"*30)
        nroProductos = int(input("Por favor ingrese el numero de productos a gestionar: "))
        for i in range(nroProductos):
            nombre = input(f"Ingrese el nombre del producto #{i+1}: ").lower()
            precio = float(input(f"Ingrese el precio del producto #{i+1}: "))
            cantidad = int(input(f"Ingrese la cantidad del producto #{i+1}: "))
            nombreArticulo.append(nombre)
            precioArticulo.append(precio)
            cantidadArticulo.append(cantidad)
    
    elif opcion == 2:
        print()
        print("#"*30)
        print("nMODULO DE VENTAS")
        print("#"*30)
        totalVenta = 0
        numProductos = int(input("¿Cuantos productos desea facturar?: "))
        for i in range(numProductos):
            nombreProductoVenta = input("Por favor ingrese el nombre del producto a vender:").lower()
            for i in range(len(nombreArticulo)):
                if nombreArticulo[i] == nombreArticulo:
                    while True:
                        cantidadProductoVenta = int(input("Por favor ingrese la cantidad a vender dcanel producto: "))
                        if cantidadProductoVenta <= cantidadArticulo[i]:
                            subtotalArticulo = precioArticulo[i] * cantidadArticulo
                            totalVenta += subtotalArticulo
                            break  
                        else:
                            print(f"La cantidad disponible del articulo es: {cantidadArticulo[i]} und(s)")
                            print("Por favor ingrese una cantidad valida.")
                
                else:
                    print("El producto ingresado no esta en la lista de los articulos.")
                    input("Presione <Enter> para continuar")    
            
    elif opcion == 3:
        pass
    
    elif opcion == 4:
        pass
    
    elif opcion == 5:
        print("Gracias por usar nuestra aplicación, HASTA PRONTO!!")
        input("Presione <Enter> para continuar")
        break
    
    else:
        print("La opción ingresada no es valida. Por favor intente de nuevo")
        input("Presione <Enter> para continuar")
        
            
            

