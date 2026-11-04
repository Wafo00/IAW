#!/usr/bin/env python3
# Ejercicio 43: Pide una cadena y un carácter por teclado (valida que sea un carácter) y muestra cuántas veces aparece el carácter en la cadena.

cadena = input("Introduce un texto: ")
caracter = input("Introduce un carácter que figure en el texto anterior: ")

while len(caracter) != 1:
    caracter = input("Debe ser un solo carácter. Escribe un carácter: ")

veces = 0

for letra in cadena:
    if letra == caracter:
        veces = veces + 1

print(f'El caracter "{caracter}" aparece {veces} veces en "{cadena}"')