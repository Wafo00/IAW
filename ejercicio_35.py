#!/usr/bin/env python3
# Ejercicio 35: Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total de lo que pagó después de los 20 meses.

# Asumo que, dada la progresiónque indica el enunciado, se paga el doble cada mes

pago_mes = 10
total_pagado = 0

for mes in range(1, 21):
    print(f"Mes {mes}: {pago_mes} €")
    total_pagado = total_pagado + pago_mes
    pago_mes = pago_mes * 2

print(f"Total pagado por los tres Bugatti Chiron, uno para cada día laborable del mes, en 20 neses: {total_pagado} €")