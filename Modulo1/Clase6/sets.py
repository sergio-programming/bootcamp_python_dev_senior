#Forma de declara los sets
lenguajes = {"Java", "Python", "Javascript", "Rust", "Go", "C++"}

#Imprimimos el set de lenguajes
print(f"Este es el set de lenguajes de programación: {lenguajes}")

#Como saber si un lenguaje esta en el set de lenguajes
print(f"¿Esta Java en el set de lenguajes?: {"Java" in lenguajes}")
print(f"¿Esta Dart en el set de lenguajes?: {"Dart" in lenguajes}")

#Como agregar un elemento a un set
lenguajes.add("Swift")
print(f"Con add() agregamos el lenguaje 'Swift' al set de lenguajes: {lenguajes}")

#Como eliminar un elemento de un set
lenguajes.remove("Go")
print(f"Con remove() eliminamos el lenguaje 'Go' del set de lenguajes: {lenguajes}")

lenguajes.discard("Rust")
print(f"Con discard() eliminamos el lenguaje 'Rust' del set de lenguajes: {lenguajes}")