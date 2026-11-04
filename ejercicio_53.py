#!/usr/bin/env python3
# Ejercicio 53: Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.

notas = []
suma = 0

# El programa pedirá la nota indicando por cuál de las cinco vamos.
for numero in range(1, 6):
    nota = float(input(f"Nota {numero}: "))

    while nota < 0 or nota > 10:
        nota = float(input(f"La nota debe ser entre 0 y 10. Nota {numero}: "))

    notas += [nota]
    suma = suma + nota

mayor = notas[0]
menor = notas[0]

for nota in notas:
    mayor = max(mayor, nota)
    menor = min(menor, nota)
# Más limpio que usar ifs con > y <

media = suma / len(notas)

print("Notas:")
for nota in notas:
    print(f"{nota:g}")

print(f"Nota media: {media:.2f}")
print(f"Nota más alta: {mayor:g}")
print(f"Nota más baja: {menor:g}")