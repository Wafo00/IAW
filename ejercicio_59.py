#!/usr/bin/env python3
"""
Ejercicio 59
Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa que de la siguiente información:
● La temperatura media de cada día
● Los días con menos temperatura
● Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide con ella. si no existe ningún día se muestra un mensaje de información.
"""

minimas = []
maximas = []

for posicion in range(5):
    dia = posicion + 1
    minimas += [float(input(f"Día {dia}, temperatura mínima: "))]
    maximas += [float(input(f"Día {dia}, temperatura máxima: "))]

print("Temperaturas medias:")
for posicion in range(5):
    media = (minimas[posicion] + maximas[posicion]) / 2
    print(f"Día {posicion + 1}: {media:g}")

menor = minimas[0]
for valor in minimas:
    if valor < menor:
        menor = valor

print(f"La temperatura más baja es {menor:g}, en los días:")
for posicion in range(5):
    if minimas[posicion] == menor:
        print(f"Día {posicion + 1}")

buscada = float(input("Escribe una temperatura máxima a buscar: "))
encontrado = False
for posicion in range(5):
    if maximas[posicion] == buscada:
        print(f"Día {posicion + 1}")
        encontrado = True

if not encontrado:
    print("Ningún día tuvo esa temperatura máxima")