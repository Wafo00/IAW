#!/usr/bin/env python3
#Ejercicio 44: Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios), realiza un programa que cuente cuántas palabras tiene.

cadena = input("Introduce un texto: ")

palabras = len(cadena.split())

print(f"La frase tiene {palabras} palabra/s")
# Si se pusieran dos espacios, "count" contaría el segundo espacio como palabra. Con (), split busca separadores, y un espacio (o 5) es UN separador.