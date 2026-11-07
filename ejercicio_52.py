#!/usr/bin/env python3
# Ejercicio 52: Crea una lista e inicialízala con 5 cadenas de caracteres leídas por teclado. Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.

original = []
for vuelta in range(5):
    cadena = input("Escribe una cadena: ")
    original += [cadena]

inversa = []
for cadena in original:
    inversa = [cadena] + inversa

print("Lista en orden inverso:")
for cadena in inversa:
    print(cadena)