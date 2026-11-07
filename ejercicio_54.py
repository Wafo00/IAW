#!/usr/bin/env python3
# Ejercicio 54: Programa que declare una lista y la vaya llenando de números hasta que introduzcamos un número negativo. Entonces se debe imprimir  el vector (sólo los elementos introducidos).

numeros = []

numero = int(input("Escribe un número (negativo para salir): "))

while numero >= 0:
    numeros += [numero]
    numero = int(input("Escribe un número (negativo para salir): "))

print(numeros)