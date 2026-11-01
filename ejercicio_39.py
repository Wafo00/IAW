#!/usr/bin/env python3
# Ejercicio 39: Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que seleccionamos la opción de "Salir".

opcion = 0

while opcion != 5:
    print()
    print("** L.A. UNDER ALIEN ATTACK **")
    print("1. New Game")
    print("2. Load Game")
    print("3. Options")
    print("4. Help")
    print("5. Quit")
    opcion = int(input("Pick your poison: "))

    if opcion == 1:
        print("The name's Duke. You can call me 'sir'.")
    elif opcion == 2:
        print("Reloading... a hero never really dies.")
    elif opcion == 3:
        print("Options? The only option is 'more explosions'.")
    elif opcion == 4:
        print("Help? Shoot the ugly ones, kiss the pretty ones. Repeat.")
    elif opcion == 5:
        print("Come get some!")
    else:
        print("Invalid choice, pal. Try a number from 1 to 5.")