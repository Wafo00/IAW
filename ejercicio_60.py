#!/usr/bin/env python3
"""
Diseñar el algoritmo correspondiente a un programa, que:
● Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
● Carga la tabla con valores numéricos enteros.
● Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla.
"""

import random

tabla = []

for numero_fila in range(5):
    nueva_fila = []
    for numero_columna in range(5):
        nueva_fila += [random.randint(1, 9)]
    tabla += [nueva_fila]

print("Tabla:")
for fila in tabla:
    print(fila)

print()
numero = 1
for fila in tabla:
    suma = 0
    for valor in fila:
        suma = suma + valor
    print(f"Suma de la fila {numero}: {suma}")
    numero = numero + 1

print()
for columna in range(5):
    suma = 0
    for fila in tabla:
        suma = suma + fila[columna]
    print(f"Suma de la columna {columna + 1}: {suma}")