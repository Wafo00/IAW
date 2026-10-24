#!/usr/bin/env python3
# Ejercicio 12: Pide al usuario dos pares de números x1,y1 y x2,y2, que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos.

punto_x1 = float(input("Introduce x1: "))
punto_y1 = float(input("Introduce y1: "))
punto_x2 = float(input("Introduce x2: "))
punto_y2 = float(input("Introduce y2: "))

cat_1 = punto_x1 - punto_x2
cat_2 = punto_y1 - punto_y2

hip = (cat_1**2 + cat_2**2) **0.5

print(f"La distancia entre los puntos es: {hip}")