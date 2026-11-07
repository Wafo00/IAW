#!/usr/bin/env python3
# Ejercicio 57: Programa que declare tres listas 'lista1', 'lista2' y 'lista3' de cinco enteros cada uno, pida valores para 'lista1' y 'lista2' y calcule lista3=lista1+lista2.

lista1 = []
lista2 = []
lista3 = []

print("Valores para lista1:")
for vuelta in range(5):
    lista1 += [int(input("Escribe un entero: "))]

print("Valores para lista2:")
for vuelta in range(5):
    lista2 += [int(input("Escribe un entero: "))]

for posicion in range(5):
    lista3 += [lista1[posicion] + lista2[posicion]]

print("lista1:", lista1)
print("lista2:", lista2)
print("lista3:", lista3)