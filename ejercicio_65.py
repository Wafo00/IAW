#!/usr/bin/env python3
"""
Ejercicio 65: Crear un programa de ordenador para gestionar los resultados de la quiniela de fútbol. Para ello vamos a utilizar dos tablas:
● Equipos: Que es una tabla de cadenas donde guardamos en cada columna el nombre de los equipos de cada partido. En la quiniela se indican 15 partidos.
● Resultados: Es una tabla de enteros donde se indica el resultado. También tiene dos columnas, en la primera se guarda el número de goles del equipo que está guardado en la primera columna de la tabla anterior, y en la segunda los goles del otro equipo.
El programa ira pidiendo los nombres de los equipos de cada partido y el resultado del partido, a continuación se imprimirá la quiniela de esa jornada.
¿Qué modificación habría que hacer en las tablas para guardar todos los resultados de todas las jornadas de la temporada?
"""

equipos = []
resultados = []

for partido in range(15):
    print(f"Partido {partido + 1}")
    local = input("  Equipo local: ")
    visitante = input("  Equipo visitante: ")
    goles_local = int(input(f"  Goles de {local}: "))
    goles_visitante = int(input(f"  Goles de {visitante}: "))
    equipos += [[local, visitante]]
    resultados += [[goles_local, goles_visitante]]

print("Quiniela de la jornada:")
for partido in range(15):
    print(f"{equipos[partido][0]} {resultados[partido][0]} - {resultados[partido][1]} {equipos[partido][1]}")