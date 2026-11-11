#!/usr/bin/env python3
# Ejercicio 69: Escribe un programa python que pida un número por teclado y que cree un diccionario cuyas claves sean desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves.

numero = int(input("Escribe un número entero: "))

cuadrados = {}

for clave in range(1, numero +1):
    cuadrados[clave] = clave * clave

print(cuadrados)