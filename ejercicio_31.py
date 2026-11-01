#!/usr/bin/env python3
#Ejercicio 31: Escribe un programa que diga si un número introducido por teclado es o no primo. Un número primo es aquel que sólo es divisible entre él mismo y la unidad. Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número.


numero = int(input("Introduce un número entero: "))

# Asumo que los menores que 2 no son primos
es_primo = True
if numero <2:
    es_primo = False

# Se intentará dividir el número entre 2, 3, 4... hasta llegar a su raíz cuadrada, para ver si es primo
divisor = 2

while es_primo == True and divisor * divisor <= numero:
    if numero % divisor == 0:
        es_primo = False
    divisor = divisor + 1

if es_primo == True:
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")