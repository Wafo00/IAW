#!/usr/bin/env python3
# Ejercicio 27: Realizar un algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.

# Asumo tabla del 1 al 10
numero = int(input("Introduce un número (entero): "))

for n in range(1, 11):
    resultado = numero * n
    print(f"{numero} x {n} = {resultado}")