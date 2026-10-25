#!/usr/bin/env python3
# Ejercicio 18: Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

nombre = input("Nombre: ")
apel_1 = input("Primer apellido: ")
apel_2 = input("Segundo apellido (Pulsar Enter para dejarlo en blanco): ")

ini_nombre = nombre[0]
ini_apel1 = apel_1[0]
# Asumo que es posible que no haya segundo apellido, por lo que uso :1 (desde el principio hasta la posicion 1, sin incluirla)
ini_apel2 = apel_2[:1]

print(f"Las iniciales son {ini_nombre.upper()}{ini_apel1.upper()}{ini_apel2.upper()}")