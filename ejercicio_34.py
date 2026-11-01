#!/usr/bin/env python3
# Ejercicio 34: Una persona se encuentra en el kilómetro 70 de una carretera, otra se encuentra en el km 150, los coches tienen sentido opuesto y tienen la misma velocidad. Realizar un programa para determinar en qué kilómetro de esa carretera se encontrarán.

# Si la velocidad es la misma, aunque sea desconocida, se encuentran justo en el punto medio de la distancia actual de ambos
# Se asume que aunque circulen en sentidos opuestos, se acercan el uno al otro

km_coche_a = 70
km_coche_b = 150

# Si se pidiera entrada por teclado para no usar los datos del enunciado, eliminar las variables previas y usar:
# km_coche_a = float(input("Kilómetro donde está el primer coche (en el enunciado, 70): "))
# km_coche_b = float(input("Kilómetro donde está el segundo coche (en el enunciado, 150): "))

km_encuentro = (km_coche_a + km_coche_b) / 2

print(f"Se encontrarán en el km: {km_encuentro:g}")