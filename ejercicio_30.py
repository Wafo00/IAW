#!/usr/bin/env python3
# Ejercicio 30: Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.

for tabla in range(1, 6):
    print(f"Tabla del {tabla}")
    for n in range(1, 11):
        resultado = n * tabla
        print(f"{tabla} x {n} = {resultado}")
    print()