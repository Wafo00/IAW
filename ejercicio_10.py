#!/usr/bin/env python3
"""
Ejercicio 10: Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
55% del promedio de sus tres calificaciones parciales.
30% de la calificación del examen final.
15% de la calificación de un trabajo final.
"""

parcial_1 = float(input("Introduce la primera calificación parcial: "))
parcial_2 = float(input("Introduce la segunda calificación parcial: "))
parcial_3 = float(input("Introduce la tercera calificación parcial: "))
ex_final = float(input("Introduce la calificación del examen final: "))
trab_final = float(input("Introduce la calificación del trabajo final: "))

peso_parciales = 0.55
peso_ex_final = 0.30
peso_trab_final = 0.15

promedio_parc = (parcial_1 + parcial_2 + parcial_3) / 3
aporte_parciales = promedio_parc * peso_parciales
aporte_ex_final = ex_final * peso_ex_final
aporte_trab_final = trab_final * peso_trab_final

cali_final = aporte_parciales + aporte_ex_final + aporte_trab_final

print(f"Tu calificación final en Algoritmos es: {cali_final:g}")