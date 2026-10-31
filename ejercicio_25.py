#!/usr/bin/env python3
# Ejercicio 25: Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL' en caso contrario, el programa termina cuando se introduce un espacio.

letra = input("Introduce una letra ( [espacio] para terminar): ")

while letra !=" ":
    if len(letra) != 1:
        print("Entrada no válida: introduce exactamente un carácter")
    elif letra.lower() in "aeiouáéíóúàèìòùäëïöüâêîôû":
        print("VOCAL")
    else:
        print("NO VOCAL")
    letra = input("Introduce una letra ( [espacio] para terminar): ")