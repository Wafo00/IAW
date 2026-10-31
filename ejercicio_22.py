#!/usr/bin/env python3
'''
Ejercicio 22: Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido, además de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado), si se llega al límite de intentos te muestra el número que había generado.
'''
import random

secreto = random.randint(1,100)
# print(secreto) # Solo para pruebas. Descomentar para ver el número inicial

numero = 0
intentos = 0
max_intentos = 10

while numero != secreto and intentos < max_intentos:
    numero = int(input("Adivina el número secreto: "))
    intentos = intentos + 1
    if numero < secreto:
        print(f"El número secreto es mayor. Te queda/n {max_intentos - intentos} intento/s")
    elif numero > secreto:
        print(f"El número secreto es menor. Te queda/n {max_intentos - intentos} intento/s")

if numero == secreto:
    print(f"¡Acertaste en {intentos} intento/s!")
else:
    print(f"Te has quedado sin intentos. El número secreto era {secreto}")