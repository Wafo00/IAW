#!/usr/bin/env python3
# Ejercicio 55: Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), y posteriormente ordene los elementos de menor a mayor.

import random

numeros = []
for vuelta in range(10):
    numeros += [random.randint(1, 42)]

print("Desordenada:", numeros)

# numeros.sort()
# hace el mismo trabajo que el for a continuación

for vuelta in range(9):
    for posicion in range(9):
        if numeros[posicion] > numeros[posicion + 1]:
            guardado = numeros[posicion]
            numeros[posicion] = numeros[posicion + 1]
            numeros[posicion + 1] = guardado

print("Ordenada:", numeros)