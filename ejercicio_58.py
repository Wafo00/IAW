#!/usr/bin/env python3
"""
Ejercicio 58: Queremos guardar los nombres y las edades de los alumnos de un curso. Realiza un programa que introduzca el nombre y la edad de cada alumno. El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*) Al finalizar se mostrará los siguientes datos:
● Todos los alumnos mayores de edad.
● Los alumnos mayores (los que tienen más edad)
"""

nombres = []
edades = []

nombre = input("Nombre del alumno (* para salir): ")

while nombre != "*":
    edad = int(input(f"Edad de {nombre}: "))
    nombres += [nombre]
    edades += [edad]
    nombre = input("Nombre del alumno (* para salir): ")

print()
print("Alumnos mayores de edad:")
for posicion in range(len(nombres)):
    if edades[posicion] >= 18:
        print(f"  {nombres[posicion]} ({edades[posicion]} años)")

if len(edades) > 0:
    edad_maxima = max(edades)
    print()
    print(f"Alumnos con más edad ({edad_maxima} años):")
    # Se puede reutilizar "posicion": el nuevo for la reinicia desde 0 y sobrescribe el valor que tenía
    for posicion in range(len(nombres)):
        if edades[posicion] == edad_maxima:
            print(f"  {nombres[posicion]}")