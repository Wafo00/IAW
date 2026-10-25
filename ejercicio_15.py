#!/usr/bin/env python3
# Ejercicio 15: Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuánto valen al final las dos variables.

A = float(input("Escribe la variable A: "))
B = float(input("Escribe la variable B: "))

C = A
A = B
B = C


print(f"Ahora la variable A vale {A:g} y la B vale {B:g}")

# En un entorno real, Python permite hacerlo sin una tercera variable con A, B = B, A