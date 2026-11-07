#!/usr/bin/env python3
"""
Vamos a crear un programa que tenga el siguiente menú:
1. Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
2. Añadir número de la lista en una posición: Me pide un número y una posición, y si la posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
3. Longitud de la lista: te muestra el número de elementos de la lista.
4. Eliminar el último número: Muestra el último número de la lista y lo borra.
5. Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella (la posición se pide a partir de 1).
6. Contar números: Te pide un número y te dice cuantas apariciones hay en la lista.
7. Posiciones de un número: Te pide un número y te dice en que posiciones está (contando desde 1).
8. Mostrar números: Muestra los números de la lista
9. Salir
"""

numeros = []
opcion = 0

while opcion != 9:
    print()
    print("===== MENÚ =====")
    print("1. Añadir número a la lista")
    print("2. Añadir número en una posición")
    print("3. Longitud de la lista")
    print("4. Eliminar el último número")
    print("5. Eliminar un número (por posición)")
    print("6. Contar números")
    print("7. Posiciones de un número")
    print("8. Mostrar números")
    print("9. Salir")
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        numero = int(input("Número a añadir: "))
        numeros += [numero]

    elif opcion == 2:
        numero = int(input("Número a añadir: "))
        posicion = int(input("Posición (desde 1): "))
        if posicion >= 1 and posicion <= len(numeros):
            # Se parte la lista en dos y se coloca el número en medio
            numeros = numeros[:posicion - 1] + [numero] + numeros[posicion - 1:]
        else:
            print("Esa posición no existe en la lista")

    elif opcion == 3:
        print(f"La lista tiene {len(numeros)} números")

    elif opcion == 4:
        if len(numeros) > 0:
            print(f"Último número: {numeros[len(numeros) - 1]}")
            numeros = numeros[:len(numeros) - 1]
        else:
            print("La lista está vacía")

    elif opcion == 5:
        posicion = int(input("Posición a eliminar (desde 1): "))
        if posicion >= 1 and posicion <= len(numeros):
            numeros = numeros[:posicion - 1] + numeros[posicion:]
        else:
            print("Esa posición no existe en la lista")

    elif opcion == 6:
        buscado = int(input("Número a contar: "))
        veces = 0
        for numero in numeros:
            if numero == buscado:
                veces = veces + 1
        print(f"El {buscado} aparece {veces} veces")

    elif opcion == 7:
        buscado = int(input("Número a buscar: "))
        encontrado = False
        for posicion in range(len(numeros)):
            if numeros[posicion] == buscado:
                print(f"El {buscado} está en la posición {posicion + 1}")
                encontrado = True
        if not encontrado:
            print(f"El {buscado} no está en la lista")

    elif opcion == 8:
        print(numeros)

    elif opcion == 9:
        print("Saliendo")

    else:
        print("Opción no válida, elige del 1 al 9")