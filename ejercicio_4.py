#!/usr/bin/env python3
#Ejercicio 4: Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
numero_a = float(input("Indica el primer número: "))
numero_b = float(input("Indica el segundo número: "))

# Las variables que intervienen ya son float, por lo que no necesito volver a ponerlo. Tampoco uso (); el orden está claro.
suma = numero_a + numero_b 
resta = numero_a - numero_b
resta2 = numero_b - numero_a
division = numero_a / numero_b
multiplicacion = numero_a * numero_b

print(f"El resultado de la suma de los números introducidos es: {suma}.")
print(f"El de la resta del primero menos el segundo, es: {resta}.") 
print(f"El de la resta del segundo menos el primero es: {resta2}.") 
print(f"El de su división es: {division}.")
print(f"El de su multiplicación es: {multiplicacion}.")