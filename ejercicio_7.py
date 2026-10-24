#!/usr/bin/env python3
# Ejercicio 7: Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuántas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

minutos_int = int(input("Escribe el número de minutos para convertirlos a horas: "))

horas = minutos_int // 60
minutos = minutos_int % 60

print(f"{minutos_int} minutos equivalen a: {horas} hora/s y {minutos} minuto/s")