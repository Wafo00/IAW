#!/usr/bin/env python3
# Ejercicio 13: Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica. Python3 no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿cómo se puede calcular?

num = float(input("Introduce un número mayor o igual que 0: "))

r_cuad = num **0.5
r_cub = num **(1/3)

print(f"La raíz cuadrada de {num:g} es {round(r_cuad, 2):g}, y la raíz cúbica es {round(r_cub, 2):g}")