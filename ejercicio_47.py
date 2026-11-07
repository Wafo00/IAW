#!/usr/bin/env python3
# Ejercicio 47: Pide una cadena y dos caracteres por teclado (valida que sea un carácter), sustituye la aparición del primer carácter en la cadena por el segundo carácter.

cadena = input("Escribe un texto: ")
buscado = input("Carácter a sustituir: ")

while len(buscado) != 1:
    buscado = input("Debe ser un solo carácter. Carácter a sustituir: ")

nuevo = input("Carácter nuevo: ")

while len(nuevo) != 1:
    nuevo = input("Debe ser un solo carácter. Carácter nuevo: ")

resultado = ""

for letra in cadena:
    if letra == buscado:
        resultado = resultado + nuevo
    else:
        resultado = resultado + letra

print(f"Resultado: {resultado}")