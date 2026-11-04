#!/usr/bin/env python3
# Ejercicio 56: Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar listas. Para simplificarlo vamos a suponer que febrero tiene 28 días.

nombres_meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

mes = int(input("Introduce número de mes: "))

while mes < 1 or mes > 12:
    mes = int(input("El número debe ser entre 1 y 12: "))

posicion = mes - 1

print(f"El mes {mes} es {nombres_meses[posicion]} y tiene {dias_meses[posicion]} días")