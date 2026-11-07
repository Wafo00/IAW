#!/usr/bin/env python3
# Ejercicio 48: Realizar un programa que lea una cadena por teclado y convierta las mayúsculas a minúsculas y viceversa.

cadena = input("Escribe un texto o cadena cualquiera: ")

resultado = ""

for letra in cadena:
    # Si .lower() la cambia, era mayúscula; si .upper() la cambia, era minúscula
    if letra != letra.lower():
        resultado = resultado + letra.lower()
    elif letra != letra.upper():
        resultado = resultado + letra.upper()
    else:
        resultado = resultado + letra

print(f"Resultado: {resultado}")