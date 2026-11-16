#!/usr/bin/env python3
# Ejercicio 75: Crea un función EscribirCentrado, que reciba como parámetro un texto y lo escriba centrado en pantalla (suponiendo una anchura de 80 columnas; pista: deberás escribir 40 - longitud/2 espacios antes del texto). Además subraya el mensaje utilizando el carácter =.

def EscribirCentrado(texto):
    espacios = 40 - len(texto) // 2
    print(" " * espacios + texto)
    print(" " * espacios + "=" * len(texto))
 
 
texto = input("Escribe un texto: ")
EscribirCentrado(texto)