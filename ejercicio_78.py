#!/usr/bin/env python3
"""Ejercicio 78: Escribir dos funciones que permitan calcular:
● La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
● La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a segundos, convertir a horas,minutos y segundos o salir del programa.
"""

 
def ASegundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos
 
 
def AHorasMinutosSegundos(total):
    horas = total // 3600
    minutos = total % 3600 // 60
    segundos = total % 60
    return horas, minutos, segundos
 
 
opcion = ""
while opcion != "3":
    print()
    print("1. Convertir a segundos")
    print("2. Convertir a horas, minutos y segundos")
    print("3. Salir")
    opcion = input("Elige una opción: ")
 
    if opcion == "1":
        horas = int(input("Horas: "))
        minutos = int(input("Minutos: "))
        segundos = int(input("Segundos: "))
        print(f"Total: {ASegundos(horas, minutos, segundos)} segundos")
    elif opcion == "2":
        total = int(input("Segundos: "))
        horas, minutos, segundos = AHorasMinutosSegundos(total)
        # Recoge, EN ORDEN, los tres valores que devuelve la función
        # Estas tres variables NO SON LAS MISMAS que las de la función, que son locales.
        print(f"{horas} h, {minutos} min, {segundos} s")
    elif opcion != "3":
        print("Opción no válida")