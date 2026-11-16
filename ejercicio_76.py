#!/usr/bin/env python3
# Ejercicio 76 : Crea un programa que pida dos números enteros al usuario y diga si alguno de ellos es múltiplo del otro. Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo.

def EsMultiplo(numero1, numero2):
    return numero1 % numero2 == 0
 
numero1 = int(input("Primer número: "))
numero2 = int(input("Segundo número: "))
 
if EsMultiplo(numero1, numero2):
    print(f"{numero1} es múltiplo de {numero2}")
elif EsMultiplo(numero2, numero1):
    print(f"{numero2} es múltiplo de {numero1}")
else:
    print("Ninguno es múltiplo del otro")