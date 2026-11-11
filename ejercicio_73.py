#!/usr/bin/env python3
"""
Ejercicio 73: Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y números de teléfono. El programa nos dará el siguiente menú:
● Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
● Buscar: Nos pide una cadena de caracteres, y nos muestra todos los contactos cuyos nombres comiencen por dicha cadena.
● Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
● Listar: Nos muestra todos los contactos de la agenda.
Implementar el programa con un diccionario.
"""

agenda = {}

opcion = "0"

while opcion != "5":
    print()
    print("1. Añadir/Modificar")
    print("2. Buscar")
    print("3. Borrar")
    print("4. Listar")
    print("5. Salir")
    opcion = (input("Elige una opción: "))

# Se introduce deliberadamente como cadena de texto, para controlar fácilmente si se introduce algo que no coincida con las opciones (ver el último elif)
    if opcion == "1":
        nombre = input("Nombre: ")
        if nombre in agenda:
            print(f"El teléfono de {nombre} es {agenda[nombre]}")
            respuesta = input("¿Quieres modificarlo? (s/n): ")
            if respuesta.lower() == "s":
                agenda[nombre] = input("Nuevo teléfono: ")
        else:
            agenda[nombre] = input("Teléfono: ")

    elif opcion == "2":
        busqueda = input("Nombres que empiecen por: ")
        for nombre in agenda:
            if nombre.lower().startswith(busqueda.lower()):
                print(nombre, agenda[nombre])

    elif opcion == "3":
        nombre = input("Nombre a borrar: ")
        if nombre in agenda:
            respuesta = input(f"Borrar {nombre}? (s/n): ")
            if respuesta.lower() == "s":
                del agenda[nombre]
        else:
            print("Ese nombre no existe")

    elif opcion == "4":
        for nombre in agenda:
            print(nombre, agenda[nombre])

    elif opcion != "5":
        print("Opción no válida")