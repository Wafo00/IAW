#!/usr/bin/env python3
#Ejercicio 2: Calcular el perímetro y área de un rectángulo dada su base y su altura.
base=float ( input("Longitud de la base: ") )
altura=float ( input("Longitud de la altura: ") )

perimetro = 2*(base+altura)
area = base*altura
print(f"El perímetro es {perimetro} y el área es {area}")