def agregarPedido(pedidos: list[str], nuevoPedido: str) -> list[str]:
    pedidos.append(nuevoPedido)
    return pedidos

def eliminarPedido(pedidos: list[str], pedido_a_eliminar: str) -> list[str]:
    if pedido_a_eliminar in pedidos:
        pedidos.remove(pedido_a_eliminar)
    else:
        print("El pedido a eliminar no se encuentra registrado")
    return pedidos

def buscarPedido(pedidos: list[str], pedidoBuscado: str) -> int:
    if pedidoBuscado in pedidos:
        return pedidos.index(pedidoBuscado)
    else:
        print("El pedido no se encuentra en la lista")
        return -1
    
def main():
    pedidosTienda = ["Pedido 1", "Pedido 3"]
    
    pedidosTienda = agregarPedido(pedidosTienda, "Pedido 2")
    
    pedidosTienda.sort()
    print(f"Lista actualizada de pedidos: {pedidosTienda}")
    
    pedidoBuscado = buscarPedido(pedidosTienda, "Pedido 2")
    print(f"El {pedidosTienda[pedidoBuscado]} esta en el indice {pedidoBuscado}")
    
    pedido_a_eliminar = "Pedido 3"
    pedidosTienda = eliminarPedido(pedidosTienda, pedido_a_eliminar)
    print(f"Lista actualizada de pedidos: {pedidosTienda}")
    
if __name__ == "__main__":
    main()
        