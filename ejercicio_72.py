#!/usr/bin/env python3
"""
Ejercicio 72
Codifica un programa en python que nos permita guardar los nombres de los alumnos de una clase y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. Guarda la información en un diccionario cuya claves serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno. 
El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo. Al final el programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error.
"""

alumnos = {}

cantidad = int(input("Número de alumnos a introducir: "))

for contador in range(cantidad):
    nombre = input("Nombre del alumno: ")
    while nombre in alumnos:
        print("Ese alumno ya existe")
        nombre = input("Nombre del alumno: ")

    notas = []
    nota = float(input("Nota (negativa para terminar): "))
    while nota >= 0:
        notas.append(nota)
        nota = float(input("Nota (negativa para terminar): "))

    alumnos[nombre] = notas

for nombre in alumnos:
    notas = alumnos[nombre]
    if len(notas) > 0:
        media = sum(notas) / len(notas)
        print(f"{nombre}: nota media {media:.2f}")
    else:
        print(f"{nombre}: sin notas")