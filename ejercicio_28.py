#!/usr/bin/env python3
"""
Ejercicio 28: Escribe un programa que pida el límite inferior y superior de un intervalo. Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introducimos el 0. Cuando termine el programa dará las siguientes informaciones:
● La suma de los números que están dentro del intervalo (intervalo abierto).
● Cuántos números están fuera del intervalo.
● Si hemos introducido algún número igual a los límites del intervalo.
"""
# El 0 termina la entrada, así que nunca puede introducirse como número (aunque el intervalo lo contenga)

inferior = int(input("Límite inferior: "))
superior = int(input("Límite superior: "))

while inferior > superior:
    print("El límite inferior no puede ser mayor que el superior")
    inferior = int(input("Límite inferior: "))
    superior = int(input("Límite superior: "))

suma_dentro = 0
fuera = 0
limite_inf= False
limite_sup = False

numero = float(input("Introduce un número (0 para terminar): "))

while numero != 0:
    if numero > inferior and numero < superior:
        suma_dentro = suma_dentro + numero
    elif numero == inferior:
        limite_inf = True
    elif numero == superior:
        limite_sup = True
    else:
        fuera = fuera + 1
    numero = float(input("Introduce un número (0 para terminar): "))

print(f"Suma de los números dentro del intervalo: {suma_dentro:g}")
print(f"Números fuera del intervalo: {fuera}")

if limite_inf:
    print(f"Has introducido el límite inferior ({inferior})")
if limite_sup:
    print(f"Has introducido el límite superior ({superior})")
if limite_inf == False and limite_sup == False:
    print("No has introducido ningún límite")
# Podría usarse "if not limite_inf and not limite_sup:", pero aún no sé cuál me resulta más legible