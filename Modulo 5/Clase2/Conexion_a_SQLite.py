import sqlite3

conexion = sqlite3.connect("academiadevsenior.db") # Conexion a base de datos SQLite

# Verificar si la conexión fue exitosa
if conexion:
    print("Conectado con SQLite.py")

# Creamos un cursor
cursor = conexion.cursor()

# Realizamos un SELECT
cursor.execute("SELECT * FROM profesores")
resultados = cursor.fetchall()

for resultado in resultados:
    print(resultado)

"""    
query = "INSERT INTO profesores (nombre, especialidad, experiencia) values (?, ?, ?)"
valores = ("Juan Triana", "Python", 10)
cursor.execute(query, valores)
conexion.commit() # Guarda los cambios
print(f"Fila insertada: {cursor.rowcount}")
"""

"""    
query = "INSERT INTO profesores (nombre, especialidad, experiencia) values (?, ?, ?)"
valores = ("Juan Triana", "Python", 10)
cursor.execute(query, valores)
conexion.commit() # Guarda los cambios
print(f"Fila insertada: {cursor.rowcount}")
"""

"""
query = "INSERT INTO cursos (nombre, profesor_id) values (?, ?)"
valores = ("Python de cero a Senior", 2)
cursor.execute(query, valores)
conexion.commit() # Guarda los cambios
print(f"Fila insertada: {cursor.rowcount}")
"""

"""
query = "UPDATE profesores SET especialidad = ? WHERE id_profesor = ?"
valores = ("Java", 1)
cursor.execute(query, valores)
conexion.commit() # Guarda los cambios
print(f"Fila actualizada: {cursor.rowcount}")
"""

query = "UPDATE cursos SET nombre = ? WHERE id_cursor = ?"
valores = ("Java la ruta maestra del codigo", 1)
cursor.execute(query, valores)
conexion.commit() # Guarda los cambios
print(f"Fila actualizada: {cursor.rowcount}")

# Cerrar cursor y conexion
cursor.close()
conexion.close()