#!/usr/bin/env python3
# Ejercicio 27: Realizar un algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.

# Asumo tablas del 1 al 10, aunque el enunciado no pide limitarlas
numero = int(input("Introduce un número (entero) del 1 al 10: "))

while numero < 1 or numero > 10:
    print("Número fuera de rango")
    numero = int(input("Introduce un número (entero) del 1 al 10: "))

for n in range(1, 11):
    resultado = numero * n
    print(f"{numero} x {n} = {resultado}")