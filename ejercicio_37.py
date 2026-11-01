#!/usr/bin/env python3
# Ejercicio 37: Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. Para esto, se registran los días que trabajó y las horas de cada día. Realice un algoritmo para determinar el sueldo semanal de N trabajadores y además calcule cuánto pagó la empresa por los N empleados.

# Asumiendo que todos los trabajadores cobran lo mismo por hora
precio_hora = float(input("Precio por hora (€): "))
cant_trabajadores = int(input("Número de trabajadores: "))

total_empresa = 0

for trabajador in range(1, cant_trabajadores + 1):
    dias_trabajados = int(input(f"Días trabajados por el trabajador {trabajador} esta semana: "))
    horas_semana = 0

    for dia in range(1, dias_trabajados + 1):
        horas_dia = float(input(f"Horas trabajadas el día {dia}: "))
        horas_semana = horas_semana + horas_dia

    sueldo = precio_hora * horas_semana
    print(f"Sueldo semanal del trabajador {trabajador}: {sueldo:.2f} €")
    total_empresa = total_empresa + sueldo

print(f"Total pagado por la empresa: {total_empresa:.2f} €")