""""
Los operadores relacionales sirven para realizar comparaciones entre dos o mas valores
Mayor que: >
Menor que: <
Mayor o igual que: >=
Menor o igual que: <=
Igual que: ==
Diferente que: !=
"""

a = 12
b = 16
c = 10
d = 14
e = 16

comparacion1 = a < d
comparacion2 = a > b
comparacion3 = a <= c
comparacion4 = b >= d
comparacion5 = b == e
comparacion6 = b != e
comparacion7 = d != e

print(f"¿{a} es menor que {b}?: {comparacion1}")
print(f"¿{a} es mayor que {b}?: {comparacion2}")
print(f"¿{a} es menor igual que {c}?: {comparacion3}")
print(f"¿{b} es mayor igual que {d}?: {comparacion4}")
print(f"¿{b} es igual que {e}?: {comparacion5}")
print(f"¿{b} es diferente a {e}?: {comparacion6}")
print(f"¿{d} es diferente a {e}?: {comparacion7}")