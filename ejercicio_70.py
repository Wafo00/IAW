#!/usr/bin/env python3
# Ejercicio 70: Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena.

cadena = input("Escribe una cadena: ")

apariciones = {}

for caracter in cadena:
    apariciones[caracter] = cadena.count(caracter)

print (apariciones)