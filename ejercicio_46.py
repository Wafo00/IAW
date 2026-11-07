#!/usr/bin/env python3
# Ejercicio 46: Realizar un programa que dada una cadena de caracteres por caracteres, genere otra cadena resultado de invertir la primera.

cadena = input("Escribe un texto o cadena de caracteres cualquiera: ")

invertida = ""

for letra in cadena:
    invertida = letra + invertida

print(f"Cadena invertida: {invertida}")