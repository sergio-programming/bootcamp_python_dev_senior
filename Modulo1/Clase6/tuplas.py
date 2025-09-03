#Forma de declarar una lista: nombreTupla = ("elemento1", "elemento2",...)
paises = ("Colombia", "Mexico", "Ecuador", "Argentina", "Brasil")

#Imprimimos la tupla
print(f"Esta es la tupla de paises: {paises}")

#Forma de acceder a un elemento de una tupla
print(f"El pais en la posición #4 es: {paises[3]}")

#Con len() imprimimos la cantidad de elementos que tiene la tupla
print(f"La tupla de paises contiene: {len(paises)} paises") 

#Imprimir la lista de paises con un for
i = 1
for pais in paises:
    print(f"Pais #{i}: {pais}")
    i+=1
    
