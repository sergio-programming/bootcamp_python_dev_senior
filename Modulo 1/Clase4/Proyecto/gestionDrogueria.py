#Variable para almacenar las ventas totales
ventasTotales = 0.0

#Listas para almacenar los productos
nombreArticulo = []
precioArticulo = []
cantidadArticulo = []

while True:
    print()
    print("#"*30)
    print("BIENVENIDOS A DROGAS LA ECONOMICA")
    print("#"*30)
    print("""1. Configuracion de productos.
2. Venta de productos.
3. Mostrar inventario
4. Mostrar ventas totales.
5. Salir del programa.""")
    
    opcion = int(input("\nPor favor digite una opcion: "))
    
    if opcion == 1:
        print()
        print("#"*30)
        print("MODULO GESTION DE PRODUCTOS")
        print("#"*30)
        nroProductos = int(input("Por favor ingrese el numero de productos a gestionar: "))
        for i in range(nroProductos):
            nombre = input(f"\nIngrese el nombre del producto #{i+1}: ").lower()
            precio = float(input(f"Ingrese el precio del producto #{i+1}: "))
            cantidad = int(input(f"Ingrese la cantidad del producto #{i+1}: "))
            nombreArticulo.append(nombre)
            precioArticulo.append(precio)
            cantidadArticulo.append(cantidad)
    
    elif opcion == 2:
        print()
        print("#"*30)
        print("MODULO DE VENTAS")
        print("#"*30)
        totalVenta = 0
        numProductos = int(input("¿Cuantos productos desea facturar?: "))
        for i in range(numProductos):
            nombreProductoVenta = input("Por favor ingrese el nombre del producto a vender: ").lower()
            for i in range(len(nombreArticulo)):
                if nombreArticulo[i] == nombreProductoVenta:
                    while True:
                        cantidadProductoVenta = int(input("Por favor ingrese la cantidad a vender del producto: "))
                        if cantidadProductoVenta <= cantidadArticulo[i]:
                            subtotalArticulo = precioArticulo[i] * cantidadProductoVenta
                            cantidadArticulo[i] -= cantidadProductoVenta
                            totalVenta += subtotalArticulo
                            break                              
                        else:
                            print(f"La cantidad disponible del articulo es: {cantidadArticulo[i]} und(s)")
                            print("Por favor ingrese una cantidad valida.")
                    break
            if nombreProductoVenta not in nombreArticulo:
                print("El producto ingresado no esta en la lista de los articulos.")
                input("Presione <Enter> para continuar")
                    
        ventasTotales += totalVenta        
        print(f"""\n<<<<<<<RESUMEN DE LA VENTA>>>>>>
Total facturado: ${totalVenta} pesos""")    
            
    elif opcion == 3:
        print()
        print("#"*30)
        print("MODULO DE INVENTARIOS")
        print("#"*30)
        if len(nombreArticulo) > 0:
            print("\nEsta es la lista de productos en el catalogo:")
            for i in range(len(nombreArticulo)):
                print(f"""\nNombre de articulo: {nombreArticulo[i]}
Precio de articulo: ${precioArticulo[i]}
Cantidad en inventario: {cantidadArticulo[i]}""")
            input("Presione <Enter> para continuar")            
        else:
            print("\nNo hay articulos actualmente en inventario")
            input("Presione <Enter> para continuar")
    
    elif opcion == 4:
        print()
        print("#"*30)
        print("MODULO VENTAS TOTALES")
        print("#"*30)
        print(f"\nTotal Vendido: ${ventasTotales} pesos")
        input("Presione <Enter> para continuar")
    
    elif opcion == 5:
        print("\nGracias por usar nuestra aplicación, HASTA PRONTO!!")
        input("Presione <Enter> para continuar")
        break
    
    else:
        print("\nLa opción ingresada no es valida. Por favor intente de nuevo")
        input("Presione <Enter> para continuar")
        
            
            

