#!/usr/bin/env python3
#Ejercicio 3: Dados los catetos de un triángulo rectángulo, calcular su hipotenusa. (c^2=a^2+b^2)
cateto_a= float (input ("Longitud del cateto a: "))
cateto_b= float (input ("Longitud del cateto b: "))

hipotenusa=(cateto_a**2+cateto_b**2)**0.5
print(f"La hipotenusa mide: {hipotenusa}")