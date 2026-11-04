#!/usr/bin/env python3
# Ejercicio 42: Realizar un programa que comprueba si una cadena leída por teclado comienza por una subcadena introducida por teclado.

cadena = input("Escribe una cadena: ")
subcadena = input("Escribe la subcadena: ")

if cadena.startswith(subcadena) == True: 
#startswith ya devuelve True o False, así que "== True" no hace falta
    print(f'"{cadena}" empieza por "{subcadena}"')
else:
    print(f'"{cadena}" NO empieza por "{subcadena}"')