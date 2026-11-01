#!/usr/bin/env python3
# Ejercicio 40: Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de números primos que queremos mostrar.

# El usuario pide la CANTIDAD DE NÚMEROS PRIMOS, no calcular hasta un número primo

cantidad = int(input("Introduce la cantidad de números primos que quieres mostrar: "))

primos_mostrados = 0
numero = 2

while primos_mostrados < cantidad:
    es_primo = True
    divisor = 2

    while divisor * divisor <= numero:
        if numero % divisor == 0:
            es_primo = False
        divisor = divisor + 1

    if es_primo == True:
        print(numero)
        primos_mostrados = primos_mostrados + 1

    numero = numero + 1