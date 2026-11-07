#!/usr/bin/env python3
# Ejercicio 49: Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado.

cadena = input("Escribe un texto o cadena cualquiera: ")
subcadena = input("Escribe la subcadena a buscar: ")

if subcadena in cadena:
    print(f'"{cadena}" contiene "{subcadena}"')
else:
    print(f'"{cadena}" NO contiene "{subcadena}"')