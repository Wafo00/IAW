#!/usr/bin/env python3
# Ejercicio 50: Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra palíndroma es aquella que se lee igual adelante que atrás.

# No importan las mayúsculas ni los espacios (pero SÍ las tildes)

cadena = input("Escribe un texto o cadena: ")

valida = ""
for letra in cadena.lower():
    if letra != " ":
        valida = valida + letra

invertida = ""
for letra in valida:
    invertida = letra + invertida

if valida == invertida:
    print(f'"{cadena}" es un palíndromo')
else:
    print(f'"{cadena}" NO es un palíndromo')