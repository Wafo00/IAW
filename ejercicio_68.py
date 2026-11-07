#!/usr/bin/env python3
"""Ejercicio 68
Escribe un programa que permita crear una lista de palabras y que, a continuación, de tres opciones:
1. Contar: Me pide una cadena, y me dice cuantas veces aparece en la lista.
2. Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas las apariciones dé la primera por la segunda en la lista.
3. Eliminar: Me pide una cadena, y la elimina de la lista.
4. Mostrar: Muestra la lista de cadenas.
5. Terminar.
"""

palabras = []

palabra = input("Escribe una palabra (vacío para terminar): ")
while palabra != "":
    palabras += [palabra]
    palabra = input("Escribe una palabra (vacío para terminar): ")

opcion = 0
while opcion != 5:
    print()
    print("1. Contar")
    print("2. Modificar")
    print("3. Eliminar")
    print("4. Mostrar")
    print("5. Terminar")
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        buscada = input("Palabra a contar: ")
        veces = 0
        for palabra in palabras:
            if palabra == buscada:
                veces += 1
        print(f"'{buscada}' aparece {veces} veces")

    elif opcion == 2:
        antigua = input("Palabra a modificar: ")
        nueva = input("Palabra nueva: ")
        resultado = []
        for palabra in palabras:
            if palabra == antigua:
                resultado += [nueva]
            else:
                resultado += [palabra]
        palabras = resultado

    elif opcion == 3:
        eliminar = input("Palabra a eliminar: ")
        resultado = []
        for palabra in palabras:
            if palabra != eliminar:
                resultado += [palabra]
        palabras = resultado

    elif opcion == 4:
        print(palabras)