#!/usr/bin/env python3
# Ejercicio 29: Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.

base = float(input("Escribe la base: "))
exponente = int(input("Escribe el exponente (número entero): "))

if base == 0 and exponente < 0:
    print("0 elevado a un exponente negativo no se puede calcular")
else:
# Esto actúa como salvaguarda en el caso en que se intente forzar una operación que no puede hacerse
    resultado = 1
    contador = 0

    while contador < abs(exponente):
        contador = contador + 1
        resultado = resultado * base

    if exponente < 0:
        resultado = 1 / resultado

    print(f"El resultado es: {resultado:g}")
# :g redondea a 6 cifras y pasa a notación científica con resultados grandes
# He incluido exponentes negativos porque no he leído bien el enunciado. Conservo el código como aprendizaje