#!/usr/bin/env python3
#Ejercicio 26: Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

numero_ini = int(input("Introduce el primer número (entero): "))
numero_fin = int(input("Introduce el segundo número (entero mayor que el primero): "))

# Recordando que el último número de un rango no se tiene en cuenta, le sumo 1
for n in range(numero_ini, numero_fin + 1):
    if n % 2 == 0:
        print(n)