#!/usr/bin/env python3
# Ejercicio 20: Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).

valor_2e = 200
valor_1e = 100
valor_50c = 50
valor_20c = 20
valor_10c = 10
valor_5c = 5
valor_2c = 2
valor_1c = 1

mon_2e = int(input("Monedas de 2€: "))
mon_1e = int(input("Monedas de 1€: "))
mon_50c = int(input("Monedas de 50 cts: "))
mon_20c = int(input("Monedas de 20 cts: "))
mon_10c = int(input("Monedas de 10 cts: "))
mon_5c = int(input("Monedas de 5 cts: "))
mon_2c = int(input("Monedas de 2 cts: "))
mon_1c = int(input("Monedas de 1 ct: "))

total_2e = valor_2e * mon_2e
total_1e = valor_1e * mon_1e
total_50c = valor_50c * mon_50c
total_20c = valor_20c * mon_20c
total_10c = valor_10c * mon_10c
total_5c = valor_5c * mon_5c
total_2c = valor_2c * mon_2c
total_1c = valor_1c * mon_1c

final = total_2e + total_1e + total_50c + total_20c + total_10c + total_5c + total_2c + total_1c

final_e = final // 100
final_cts = final % 100

print(f"El total asciende a {final_e} € con {final_cts} céntimos")

# He añadido las monedas de 5, 2 y 1 céntimo porque me gustan las huelgas japonesas.