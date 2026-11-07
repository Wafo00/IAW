#!/usr/bin/env python3
"""
Ejercicio 62: Diseñar el algoritmo correspondiente a un programa, que:
● Crea una tabla bidimensional de longitud 5x15 y nombre 'marco'.
● Carga la tabla con dos únicos valores 0 y 1, donde el valor uno ocupará las posiciones o elementos que delimitan la tabla, es decir, las más externas, mientras que el resto de los elementos contendrán el valor 0.
111111111111111
100000000000001
100000000000001
100000000000001
111111111111111
● Visualiza el contenido de la matriz en pantalla.
"""

marco = []

for fila in range(5):
    nueva_fila = []
    for columna in range(15):
        if fila == 0 or fila == 4 or columna == 0 or columna == 14:
            nueva_fila += [1]
        else:
            nueva_fila += [0]
    marco += [nueva_fila]

for fila in marco:
    linea = ""
    for valor in fila:
        linea += str(valor)
    print(linea)