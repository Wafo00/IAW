#!/usr/bin/env python3
# Ejercicio 67: Crear un programa que añada números a una lista hasta que introducimos un número negativo. A continuación debe crear una nueva lista igual que la anterior pero eliminando los números duplicados. Muestra esta segunda lista para comprobar que hemos eliminado los duplicados.

numeros = []

numero = int(input("Escribe un número (negativo para terminar): "))
while numero >= 0:
    numeros += [numero]
    numero = int(input("Escribe un número (negativo para terminar): "))

sin_duplicados = []
for numero in numeros:
    if numero not in sin_duplicados:
        sin_duplicados += [numero]

print(sin_duplicados)