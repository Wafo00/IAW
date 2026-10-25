#!/usr/bin/env python3
# Ejercicio 16: Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar en qué tiempo (minutos) alcanzará el vehículo más rápido al otro.

# Sin usar if, se indica al usuario que la velocidad del de atrás debe ser mayor
v_detras = float(input("Introduce la velocidad del vehículo de atrás en km/h (mayor que la del de delante): "))
v_delante = float(input("Introduce la velocidad del vehículo de delante en km/h (menor que la del de detrás): "))
d = float(input("Introduce la distancia entre los vehículos en km: "))

t_min = (d / (v_detras - v_delante)) * 60

print(f"El vehículo de atrás alcanzará al de delante en {t_min:.2f} minutos.")