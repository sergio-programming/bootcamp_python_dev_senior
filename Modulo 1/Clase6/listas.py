#Forma de declarar listas: nombreLista = ["elemento1", "elemento2",...]
nombres = ["Sergio", "Luisa", "Valentina", "Jorge", "Jenifer"]

#Imprimir la lista
print(nombres)
#Imprimir el tipo de dato
print(type(nombres))

#Forma de acceder a un elemento a traves del indice
print(f"Este es el nombre en la posicion #1: {nombres[1]}")

#Forma de segmentar elementos de una lista
print(f"Estos son los nombres de la posicion 1 a la 3: {nombres[1:4]}")

#Con el metodo len() podemos averiguar la longitud de la lista
print(f"La lista nombres contiene: {len(nombres)} elementos")

#Con el metodo append() se agrega un elemento al final de la lista
nombres.append("Karen")
print(f"Con append agregamos un nombre al final de la lista: {nombres}")

#Con el metodo insert agregamos un elemento a la lista en el indice especificado
nombres.insert(2, "Diego")
nombres.insert(4, "Lady")
print(f"Con insert, agregamos a Diego en la posicion 3 y a Lady 5 de la lista: {nombres}")

#Con el metodo pop() eliminamos el ultimo elemento de la lista
nombres.pop()
print(f"Con pop eliminamos el ultimo elemento de la lista: {nombres}")

#Con el metodo del [lista] eliminamos el elemento del indice especificado
del nombres[2]
print(f"Con del [lista] vamos a eliminar al elemento en la posición 3 (Diego): {nombres}")

#Con el metodo sort() ordenamos los elementos de una lista
nombres.sort()
print(nombres)
