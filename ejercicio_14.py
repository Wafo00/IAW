#!/usr/bin/env python3
# Ejercicio 14: Dado un número de dos cifras, diseña un algoritmo que permita obtener el número invertido. Ejemplo, si se introduce 23 que muestre 32.

entrada = int(input("Introduce un número ENTERO y POSITIVO de dos cifras: "))

primera = entrada // 10
segunda = entrada % 10

print(f"El número invertido de {entrada} es {segunda}{primera}")
# El enunciado no aclara si hay que mostrar el resultado como texto o como número, de tal modo que, si pongo "50", el invertido será "05". Para hacerlo numéricamente haría falta una variable nueva, por ejemplo: invertido = segunda * 10 + primera