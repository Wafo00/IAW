#!/usr/bin/env python3
# Ejercicio 33: Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la semana (seis días) y requiere determinar el total de éstas, así como el sueldo que recibirá por las horas trabajadas.

# No se indica el precio por hora. Se le pide al usuario
precio_hora = float(input("Precio por hora (€): "))
total_horas = 0

for dia in range(1, 7):
    horas = float(input(f"Horas trabajadas el día {dia}: "))
    total_horas = total_horas + horas

sueldo = precio_hora * total_horas

print(f"Total de horas trabajadas de la semana: {total_horas:g}")
print(f"Sueldo semanal: {sueldo:.2f} €")