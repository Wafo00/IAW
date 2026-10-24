#!/usr/bin/env python3
# Ejercicio 9: Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra.

importe_compra = float(input("Introduce el valor de la compra sin descuento: "))

# Aunque el enunciado fija el 15%, el programa sirve para cualquier porcentaje
porcentaje = float(input("Introduce el porcentaje del descuento (solo el número): "))

dto = porcentaje / 100
valor_dto = importe_compra * dto
total = importe_compra - valor_dto

print(f"Aplicando un descuento del {porcentaje} %, se descuentan {valor_dto:.2f} €")
print(f"El total a pagar es {total:.2f} €")