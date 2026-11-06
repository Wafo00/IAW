#!/usr/bin/env python3
"""
Ejercicio 64: Crear un programa que lea los precios de 5 artículos y las cantidades vendidas por una empresa en sus 4 sucursales. Informar:
● Las cantidades totales de cada artículo.
● La cantidad de artículos en la sucursal 2.
● La cantidad del artículo 3 en la sucursal 1.
● La recaudación total de cada sucursal.
● La recaudación total de la empresa.
● La sucursal de mayor recaudación.
"""

precios = []
for articulo in range(5):
    precios += [float(input(f"Precio del artículo {articulo + 1}: "))]

cantidades = []
for sucursal in range(4):
    fila = []
    for articulo in range(5):
        fila += [int(input(f"Sucursal {sucursal + 1}, unidades vendidas del artículo {articulo + 1}: "))]
    cantidades += [fila]

print()
print("Cantidades totales de cada artículo:")
for articulo in range(5):
    total = 0
    for fila in cantidades:
        total = total + fila[articulo]
    print(f"  Artículo {articulo + 1}: {total}")

total_sucursal_2 = 0
for cantidad in cantidades[1]:
    total_sucursal_2 = total_sucursal_2 + cantidad
print(f"Cantidad de artículos en la sucursal 2: {total_sucursal_2}")

print(f"Cantidad del artículo 3 en la sucursal 1: {cantidades[0][2]}")

print()
print("Recaudación de cada sucursal:")
recaudacion_empresa = 0
mayor_recaudacion = -1
sucursal_mayor = 0

for sucursal in range(4):
    recaudacion = 0
    for articulo in range(5):
        recaudacion = recaudacion + cantidades[sucursal][articulo] * precios[articulo]
    print(f"  Sucursal {sucursal + 1}: {recaudacion:.2f} €")
    recaudacion_empresa = recaudacion_empresa + recaudacion

    if recaudacion > mayor_recaudacion:
        mayor_recaudacion = recaudacion
        sucursal_mayor = sucursal + 1

print(f"Recaudación total de la empresa: {recaudacion_empresa:.2f} €")
print(f"Sucursal de mayor recaudación: la {sucursal_mayor} ({mayor_recaudacion:.2f} €)")