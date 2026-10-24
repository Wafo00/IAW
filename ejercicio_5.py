#!/usr/bin/env python3
# Ejercicio 5: Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es: C = (F-32)*5/9

fahr = float(input("Introducir temperatura en grados Fahrenheit, que es una unidad de medida absurda: "))

# Ojo: fuera de una f-string, las variables se escriben tal cual, sin {}
cels = (fahr - 32) * 5 / 9

# {variable:.2f} redondea a dos decimales
print(f"La temperatura en grados Celsius es: {cels:.2f} ")