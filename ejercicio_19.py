#!/usr/bin/env python3
"""
Ejercicio 19: Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime el resultado obtenido por el estudiante.
"""
# Sin if, no se gestionan las notas negativas
# El programa está preparado para cambiar los puntos que suman y restan, a decimales
acierto = 5
fallo = (-1)

correctas = int(input("Introduzca el número de respuestas correctas: "))
falladas = int(input("Introduzca el número de respuestas incorrectas: "))

suman = correctas * acierto
restan = falladas * fallo

total = suman + restan

print(f"El resultado es: {total:g} puntos")