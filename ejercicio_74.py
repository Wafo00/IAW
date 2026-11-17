#!/usr/bin/env python3
"""
Ejercicio 74
Crea una función BuscarEjercicio que reciba un número de ejercicio y una lista con los ejercicios existentes, y devuelva si ese ejercicio existe.

En el programa principal, crea una lista con los números de los ejercicios del 1 al 78, sin incluir el 74 (el 74 nunca existió). A continuación, el programa irá pidiendo números de ejercicio hasta que el usuario escriba fin. Para cada número, indicará si el ejercicio existe o no. Si el usuario pregunta por el 74, se mostrará un mensaje.»
"""

def BuscarEjercicio(numero, ejercicios):
    return numero in ejercicios
 
 
lista_ejercicios = []
for numero in range(1, 79):
    if numero != 74:
        lista_ejercicios.append(numero)
 
texto = input("Número de ejercicio (Escribe 'fin' para salir): ")
while texto != "fin":
    numero = int(texto)
    if numero == 74:
        print("El ejercicio 74 desapareció sin dejar rastro entre los bloques 4 y 5. Consulte con su docente.")
    elif BuscarEjercicio(numero, lista_ejercicios):
        print(f"El ejercicio {numero} existe")
    else:
        print(f"El ejercicio {numero} no existe")
    texto = input("Número de ejercicio (fin para salir): ")