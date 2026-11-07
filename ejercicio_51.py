#!/usr/bin/env python3
# Ejercicio 51: Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

import random

numeros = []

for vuelta in range(10):
    numeros += [random.randint(1, 10)]

print("Número | Cuadrado | Cubo")
for numero in numeros:
    cuadrado = numero * numero
    cubo = numero * numero * numero
    print(f"{numero:6d} | {cuadrado:8d} | {cubo:4d}")
    # :6d, :8d y :4d reservan 6, 8 y 4 huecos para cada número