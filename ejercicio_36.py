#!/usr/bin/env python3
# Ejercicio 36: Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. Realice un algoritmo para determinar el sueldo semanal de N trabajadores y, además, calcule cuánto pagó la empresa por los N empleados.

# Asumiendo que todos los trabajadores cobran lo mismo por hora
precio_hora = float(input("Precio por hora (€): "))
cant_trabajadores = int(input("Número de trabajadores: "))

total_empresa = 0

for trabajador in range(1, cant_trabajadores + 1):
    horas = float(input(f"Horas trabajadas por el trabajador {trabajador} esta semana: "))
    sueldo = precio_hora * horas
    print(f"Sueldo semanal del trabajador {trabajador}: {sueldo:.2f} €")
    total_empresa = total_empresa + sueldo

print(f"Total pagado por la empresa: {total_empresa:.2f} €")