#!/usr/bin/env python3
# Ejercicio 38: Hacer un programa que muestre un cronómetro, indicando las horas, minutos y segundos. (esta vez con variables)

import time

horas , minutos , segundos = 0, 0, 0

# Bucle infinito
contador_seg = 0
while True:
    time.sleep(1)
    contador_seg += 1 
    # Es lo mismo que "var = var +1"
    horas = contador_seg // 3600
    minutos = contador_seg % 3600 // 60
    segundos = contador_seg % 60
    print(f'{horas:02d}:{minutos:02d}:{segundos:02d}')