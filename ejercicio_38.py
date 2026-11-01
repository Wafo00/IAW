#!/usr/bin/env python3
# Ejercicio 38: Hacer un programa que muestre un cronómetro, indicando las horas, minutos y segundos.

import time

# Para esperar entre cada número (reducir este número para aumentar la velocidad de los segundos del cronómetro)
pausa = 1

for horas in range(0, 24):
    for minutos in range(0, 60):
        for segundos in range(0, 60):
            print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")
            time.sleep(pausa)

# Ctrl + C para parar el programa, o esperar 24 horas