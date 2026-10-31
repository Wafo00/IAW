#!/usr/bin/env python3
#Ejercicio 24: Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

mayor0 = 0
menor0 = 0
igual0 = 0
contador = 0

cantidad = int(input("¿Cuántos números quieres introducir?: "))

while contador < cantidad:
    numero = float(input("Introduce un número: "))
    contador = contador + 1

    if numero > 0:
        mayor0 = mayor0 + 1

    elif numero < 0:
        menor0 = menor0 + 1

    else:
        igual0 = igual0 + 1

print(f"Número/s mayore/s a 0 -> {mayor0}")
print(f"Número/s menore/s a 0 -> {menor0}")
print(f"Número/s igual/es a 0 -> {igual0}")