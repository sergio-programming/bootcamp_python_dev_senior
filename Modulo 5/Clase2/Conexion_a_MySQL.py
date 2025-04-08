import mysql.connector

# Configuraciones de conexion
conexion = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="admin",
    database= "academiadevsenior"
)

# Verificar conexion con MySQL
if conexion.is_connected():
    print("Conectado con MySQL.py")

# Creamos un cursor para ejecutar una sentencia SQL
cursor = conexion.cursor()
# Ejecutar consultas SQL

# SELECT
cursor.execute("SELECT *FROM estudiantes")
results = cursor.fetchall() # Obtenemos todos los resultados
for result in results:
    print(result)
    
    
# INSERT
"""
query = "INSERT INTO profesores (nombre, especialidad, experiencia) values (%s, %s, %s)"
valores = ("Alfonso Lara", "Python", 8)
cursor.execute(query, valores)
conexion.commit() # Guarda los cambios
print(f"Fila insertada: {cursor.rowcount}")
"""

# UPDATE
"""
query = "UPDATE profesores SET experiencia = %s WHERE id_profesor = %s"
valores = (17, 1)
cursor.execute(query, valores)
conexion.commit() # Guarda los cambios
print(f"Fila insertada: {cursor.rowcount}")
"""

# DELETE
"""
query = "DELETE FROM profesores WHERE id_profesor = %s;"
valores = (3,)
cursor.execute(query, valores)
"""

# SELECT profesores
cursor.execute("SELECT *FROM profesores")
results = cursor.fetchall() # Obtenemos todos los resultados
for result in results:
    print(result)


# Cerrar cursor
cursor.close()
# Cerrar conexion con MySQL    
conexion.close()