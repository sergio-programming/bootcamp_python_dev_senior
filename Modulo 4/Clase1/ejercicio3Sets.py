from typing import Set

def obtenerClientesUnicos(clientes: Set[str], nuevosClientes: Set[str]) -> Set[str]:
    return clientes.union(nuevosClientes)

def gestionarClientes(clientes: Set[str]) -> None:
    
    # Agregar un cliente
    clientes.add("Pedro") 
    print(f"Clientes después de agregar a Pedro: {clientes}")
    
    # Agregar un cliente duplicado
    clientes.add("Carlos")
    print(f"Clientes después de agregar a Carlos: {clientes}")
    
    # Uso de la función remove para eliminar un cliente (si existe y si NO => ERROR)
    cliente = "Ana"
    clientes.remove(cliente)
    print(f"Clientes después de eliminar a {cliente} con el metodo remove: {clientes}")
    
    # Uso de la función discard para eliminar un elemento de un set
    cliente2 = "Luis"
    clientes.discard(cliente2)
    print(f"Clientes después de eliminar a {cliente2} con el metodo discard: {clientes}")
    
    #Uso del metodo pop para mostrar un elemento del Set y posterior lo borra
    cliente_a_remover = clientes.pop()
    print(f"Cliente removido aleatoriamente: {cliente_a_remover}")
    
    # Clear para borrar todos los elementos del set
    clientes.clear()
    print(f"Este es el Set de Clientes de despues del clear: {clientes}")    
    
def main():
    clientesAntiguos = {"Ana", "Maria", "Carlos", "Jaime", "Lizeth"}
    clientesNuevos = {"Luis", "Cristian", "Sandra", "Sergio", "Luisa", "Laura", "Valentina"}
    clientesFinales = obtenerClientesUnicos(clientesAntiguos, clientesNuevos)
    print(f"Este es el set definitivo de clientes: {clientesFinales}")
    
    gestionarClientes(clientesFinales)
    
if __name__ == "__main__":
    main()
    
    
