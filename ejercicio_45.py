#!/usr/bin/env python3
# Ejercicio 45: Si tenemos una cadena con un nombre y apellidos, realizar un programa que muestre las iniciales en mayúsculas.

nombre = input("Introduce nombre y apellidos: ")

iniciales = ""

for palabra in nombre.split():
    iniciales = iniciales + palabra[0].upper()

# La IA me advierte de que [0] vale aquí: (split() no da palabras vacías). Con un input() directo , recomienda, para el futuro, usar [:1] -> evitaría el error si directamente se pulsa enter.
print(f"Iniciales: {iniciales}")