#!/usr/bin/env python3
"""
Ejercicio 71: Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar los precios de las distintas frutas. El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario. Si la fruta no existe nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.
"""

precios = {"manzana": 1.5, "pera": 2, "naranja": 1.2, "plátano": 1.8}

otra = "s"
while otra == "s":
    fruta = input("Nombre de la fruta: ").lower()
    if fruta in precios:
        cantidad = int(input("Cantidad vendida: "))
        precio_final = precios[fruta] * cantidad
        print(f"El precio final de {fruta} es {precio_final:.2f}")
    else:
        print("Esa fruta no existe")
    otra = input("¿Quieres hacer otra consulta? (s/n): ").lower()