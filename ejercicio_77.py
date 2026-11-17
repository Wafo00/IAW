#!/usr/bin/env python3
"""
Ejercicio 77: Crear una subrutina llamada "Login", que recibe un nombre de usuario y una contraseña y te devuelve verdadero si el nombre de usuario es "usuario1" y la contraseña es "asdasd".
Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.
Crear un programa principal donde se pida un nombre de usuario y una contraseña y se
intente hacer login, solamente tenemos tres oportunidades para intentarlo.
"""
 
def Login(usuario, contrasena, intentos):
    if usuario == "usuario1" and contrasena == "asdasd":
        return True, intentos
    else:
        return False, intentos + 1
 
 
intentos = 0
correcto = False
 
while intentos < 3 and not correcto:
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")
    correcto, intentos = Login(usuario, contrasena, intentos)
    if not correcto:
        print(f"Datos incorrectos. Intentos: {intentos} de 3")
 
if correcto:
    print("Login correcto. Bienvenido/a")
else:
    print("Has agotado los tres intentos")