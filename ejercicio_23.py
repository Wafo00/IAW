#!/usr/bin/env python3
#Ejercicio 23: Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.

total = 0
cantidad = 0

numero = float(input("Introduce un número (0 para terminar): "))

# El siguiente número se pide al final del bucle para que el 0 no se sume ni se cuente
while numero != 0:
    total = total + numero
    cantidad = cantidad + 1
    numero = float(input("Introduce un número (0 para terminar): "))

if cantidad > 0:
    media = total / cantidad
    print(f"Suma: {total:g}")
    print(f"Media: {media:g}")
else:
    print("No has introducido ningún número")