"""
Listas (list): Son colecciones ordenadas y mutables que permiten almacenar elementos
de diferentes tipos. Se definen con [] y permiten modificar, agregar o eliminar elementos.
"""
productos = ["Carne", "Papa", "Tomate"]
productos.append("Yuca")
print(f"Esta es la lista de productos: {productos}")

"""
Tuplas (tuple): Son similares a las listas, pero inmutables, es decir, no se pueden modificar
una vez creadas. Se definen con ().
"""
empleado = (1010, "Sergio Pedraza", "Desarrollador")
print(f"Esta es una tupla con los datos del empleado: {empleado}")

#Convertir tupla a lista para poder modificar datos dentro de una tupla
empleadoList = list(empleado)
empleadoList[1] = "Johan Gordillo"
print(f"Estos son los nuevos datos del empleado que estan en una lista: {empleadoList}")

"""
Sets (set): Son colecciones desordenadas y sin elementos duplicados. Se definen con {} y son útiles
para operaciones de conjuntos como unión, intersección y diferencia.
"""
categoriasPeliculas = {"Terror", "Suspenso", "Drama"}
#Añadimos un elemento al set pero no se define para este elemento
categoriasPeliculas.add("Biografica")
print(f"Este es un set con categorias de peliculas: {categoriasPeliculas}")

"""
Diccionarios (dict): Son colecciones de pares clave-valor, ideales para almacenar datos estructurados.
Se definen con {} y permiten acceder a valores a través de sus claves.
"""
persona = {"nombre": "Sergio", "edad": 35}