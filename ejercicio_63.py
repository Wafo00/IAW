#!/usr/bin/env python3
"""
Ejercicio 63: De una empresa de transporte se quiere guardar el nombre de los conductores que tiene, y los kilómetros que conducen cada día de la semana. Para guardar esta información se van a utilizar dos listas:
● Nombre: Lista para guardar los nombres de los conductores.
● kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
Se quiere generar una nueva lista ("total_kms") con los kilómetros totales que realiza cada conductor.
Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que han realizado.
"""

cantidad = int(input("¿Cuántos conductores hay? "))

nombre = []
kms = []

for conductor in range(cantidad):
    nombre += [input(f"Nombre del conductor {conductor + 1}: ")]
    km_semana = []
    for dia in range(7):
        km_semana += [int(input(f"  Km del día {dia + 1}: "))]
    kms += [km_semana]

total_kms = []
for km_semana in kms:
    total = 0
    for km in km_semana:
        total += km
    total_kms += [total]

for posicion in range(cantidad):
    print(f"{nombre[posicion]}: {total_kms[posicion]} km")