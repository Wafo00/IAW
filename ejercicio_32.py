#!/usr/bin/env python3
# Ejercicio 32: Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si al final de cada mes deposita cantidades variables de dinero; además, se quiere saber cuánto lleva ahorrado cada mes.

ahorrado = 0

for mes in range(1, 13):
    deposito = float(input(f"Depósito del mes {mes} (€): "))
    ahorrado = ahorrado + deposito 
    print (f"Ahorrado hasta el mes {mes}: {ahorrado:.2f} (€)")

print (f"Ahorro total del año: {ahorrado:.2f} €")
