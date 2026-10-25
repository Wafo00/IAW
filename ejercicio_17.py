#!/usr/bin/env python3
#Ejercicio 17: Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.

hh = int(input("Introduce la hora de salida (HH): "))
mm = int(input("Introduce los minutos de salida (MM): "))
ss = int(input("Introduce los segundos de salida (SS): "))
t = int(input("Introduce el tiempo de viaje en segundos (T): "))

tot_seg_salida = (hh * 3600) + (mm * 60) + ss
tot_seg_llegada = tot_seg_salida + t

# Se tienen en cuenta tiempos de viaje de más de 24 horas
dias = tot_seg_llegada // 86400
resto_dia = tot_seg_llegada % 86400

h_lleg = resto_dia // 3600
resto = resto_dia % 3600

m_lleg = resto // 60
s_lleg = resto % 60

print(f"Días transcurridos: {dias}")
# Para las horas, minutos y segundos menores a 10, uso :02d para mostrar un cero delante.
print(f"La hora de llegada es: {h_lleg:02d}:{m_lleg:02d}:{s_lleg:02d}")