#!/usr/bin/env python3
# Ejercicio 8: Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas. El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

venta_1 = float(input("Introduzca el importe de la Venta 1: "))
venta_2 = float(input("Introduzca el importe de la Venta 2: "))
venta_3 = float(input("Introduzca el importe de la Venta 3: "))
salario = float(input("Introduzca su salario base: "))

# Crear la variable asegura que, si hay que cambiar el valor, solo se cambia aquí
comision = 0.1

# Aunque no lo pide el enunciado, desgloso las comisiones por cada venta
com_venta_1 = venta_1 * comision
com_venta_2 = venta_2 * comision
com_venta_3 = venta_3 * comision
total_com = com_venta_1 + com_venta_2 + com_venta_3
total = salario + total_com

print(f"El importe de las comisiones por la Venta 1 es: {com_venta_1:.2f} €")
print(f"El importe de las comisiones por la Venta 2 es: {com_venta_2:.2f} €")
print(f"El importe de las comisiones por la Venta 3 es: {com_venta_3:.2f} €")
print(f"El importe de las comisiones es: {total_com:.2f} €")
print(f"El importe a percibir es: {total:.2f} €")