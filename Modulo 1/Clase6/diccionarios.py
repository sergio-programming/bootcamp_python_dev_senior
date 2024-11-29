conceptosProgramacion = {
    "POO": "Programacion Orientada a Objetos",
    "IDE": "Entorno de Desarrollo integrado",
    "DBMS": "Sistema de gestion de bases de datos"
}

#Impresion del diccionario
print(f"Este es el diccionario: {conceptosProgramacion}")

#Longitud de diccionario
print(f"¿Cuantos pares clave-valor tiene el diccionario?: {len(conceptosProgramacion)}")

#Como acceder al valor de una key
print(f"¿Que significa POO?: {conceptosProgramacion['POO']}")
print(f"¿Que significa IDE?: {conceptosProgramacion.get('POO')}")

print("\nConceptos de Programación:")
#Como imprimir la claves y los valores de un diccionario
for key, values in conceptosProgramacion.items():
    print(f"{key}: {values}")
    
#Como modificar el valor de una clave o key
conceptosProgramacion["DBMS"] = "Database Management System"

print("\nConceptos de Programación:")
#Como imprimir la claves y los valores de un diccionario
for key, values in conceptosProgramacion.items():
    print(f"{key}: {values}")
