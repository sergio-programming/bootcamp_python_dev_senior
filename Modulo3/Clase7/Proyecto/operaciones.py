from productos import obtenerProducto

def calcularTotal(listaProductos):
    """Calcular el total de la compra"""
    total = 0
    for producto in listaProductos:
        total += producto['precio']
    return total

def agregarProducto(idProducto, cantidad, listaProductos):
    """Agregar un producto a la lista de compra"""
    producto = obtenerProducto(idProducto)
    if producto:
        listaProductos.append({"nombre": producto["nombre"], "precio": producto["precio"] * cantidad})
    else:
        raise ValueError(f"Producto con ID {idProducto} no encontrado")