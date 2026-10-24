#!/usr/bin/env python3
# Ejercicio 11: Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

num_1 = float(input("Introduce el primer número: "))
num_2 = float(input("Introduce el segundo número: "))

diferencia = num_1 - num_2
dist_absol = abs(diferencia)

print(f"La diferencia absoluta entre los números introducidos es: {dist_absol:g}")