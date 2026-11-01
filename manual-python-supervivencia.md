# Manual de supervivencia de Python

*Autor: Claude · Para consulta rápida · Nivel: principiante (UD3 de IAW)*

Cada apartado responde a una sola pregunta y lleva un ejemplo para copiar y adaptar.

**Cómo usarlo:** si se conoce el nombre de lo que se busca, ir al *Índice*. Si no, ir a la *Guía rápida* y buscar por el problema.

## Índice

**Parte I. Fundamentos**

- [1. Ejecutar un programa](#1-ejecutar-un-programa)
- [2. Variables y tipos de dato](#2-variables-y-tipos-de-dato)
- [3. Entrada y salida de datos](#3-entrada-y-salida-de-datos)
- [4. Operadores aritméticos](#4-operadores-aritméticos)

**Parte II. Control de flujo**

- [5. Condicionales: if, elif, else](#5-condicionales-if-elif-else)
- [6. Operadores de comparación y lógicos](#6-operadores-de-comparación-y-lógicos)
- [7. Variables booleanas (banderas)](#7-variables-booleanas-banderas)
- [8. Bucle for](#8-bucle-for)
- [9. Bucle while](#9-bucle-while)
- [10. Elección entre for y while](#10-elección-entre-for-y-while)

**Parte III. Técnicas y patrones**

- [11. Patrones habituales](#11-patrones-habituales)
- [12. Bucles anidados](#12-bucles-anidados)

**Parte IV. Referencia**

- [13. Cadenas de texto (strings)](#13-cadenas-de-texto-strings)
- [14. Módulos random y time](#14-módulos-random-y-time)
- [15. Errores frecuentes](#15-errores-frecuentes)
- [16. Lista de verificación antes de entregar](#16-lista-de-verificación-antes-de-entregar)

**Guía rápida**

- [¿Qué necesito? Búsqueda por problema](#guía-rápida-qué-necesito)

## Guía rápida: ¿qué necesito?

Si no se sabe cómo se llama lo que se busca, se localiza aquí por el problema.

| Quiero... | Ir al apartado |
|---|---|
| Pedir un dato o mostrar un resultado | [3](#3-entrada-y-salida-de-datos) |
| Hacer cálculos (resto, división entera, valor absoluto, potencia) | [4](#4-operadores-aritméticos) |
| Hacer algo solo si se cumple una condición | [5](#5-condicionales-if-elif-else) y [6](#6-operadores-de-comparación-y-lógicos) |
| Combinar varias condiciones (y / o / no) | [6](#6-operadores-de-comparación-y-lógicos) |
| Recordar si algo ya ha ocurrido | [7](#7-variables-booleanas-banderas) |
| Repetir algo un número fijo de veces | [8](#8-bucle-for) |
| Repetir hasta que el usuario escriba algo (por ejemplo, un 0) | [9](#9-bucle-while) |
| No sé si usar `for` o `while` | [10](#10-elección-entre-for-y-while) |
| Sumar, multiplicar o contar muchas cosas | [11](#11-patrones-habituales) |
| Hallar el mayor o el menor de varios datos | [11](#11-patrones-habituales) |
| Comprobar si un número es primo, par o múltiplo de otro | [4](#4-operadores-aritméticos) y [11](#11-patrones-habituales) |
| Calcular una potencia sin el operador de potencia | [11](#11-patrones-habituales) |
| Repetir una pregunta hasta que la respuesta sea válida | [11](#11-patrones-habituales) |
| Hacer un menú de opciones | [11](#11-patrones-habituales) |
| Repetir algo dentro de otra repetición | [12](#12-bucles-anidados) |
| Trabajar con letras, vocales o longitud de un texto | [13](#13-cadenas-de-texto-strings) |
| Generar un número al azar o hacer una pausa | [14](#14-módulos-random-y-time) |
| Entender un mensaje de error | [15](#15-errores-frecuentes) |
| Averiguar por qué el programa no termina | [9](#9-bucle-while) y [15](#15-errores-frecuentes) |
| Saber qué comprobar antes de entregar un ejercicio | [16](#16-lista-de-verificación-antes-de-entregar) |

---


## 1. Ejecutar un programa

- Windows: `py ejercicio_1.py`. Linux/macOS: `python3 ejercicio_1.py`.
- Primera línea del fichero (shebang), **sin espacios**: `#!/usr/bin/env python3`. Con `python 3` falla.
- Si ves `PS C:\...>`, el programa **ya terminó**. Lo que teclees ahora lo lee PowerShell, no Python.
- Programa colgado o que no acaba: **Ctrl + C**.
- Una línea que empieza por `#` es un comentario: Python la ignora. Úsalos para escribir suposiciones.

## 2. Variables y tipos de dato

Una variable es una caja con nombre: `edad = 30`.

| Tipo | Qué guarda | Ejemplo |
|---|---|---|
| `int` | Número entero | `7` |
| `float` | Número con decimales | `7.5` |
| `str` | Texto | `"hola"` |
| `bool` | Verdadero o falso | `True`, `False` |

- Nombres que digan lo que contienen: `total_pagado`, no `x`.
- Sin espacios ni tildes; se separa con `_`.
- Mayúsculas importan: `Total` y `total` son cajas distintas. Un solo cambio de letra crea una variable nueva (error típico).

## 3. Entrada y salida de datos

```python
nombre = input("Nombre: ")        # siempre devuelve TEXTO
edad = int(input("Edad: "))       # texto → entero
precio = float(input("Precio: ")) # texto → decimal
```

- `input` **siempre** da texto. Para operar, convertir con `int()` o `float()`.
- Mostrar: `print(...)`. Para mezclar texto y variables, **f-string** (la `f` delante de las comillas):

```python
print(f"{nombre} tiene {edad} años")
```

| Formato | Para qué | Ejemplo |
|---|---|---|
| `{x:.2f}` | 2 decimales | `3.14159` → `3.14` |
| `{x:g}` | quitar ceros sobrantes | `38.0` → `38` |
| `{x:02d}` | rellenar con ceros | `5` → `05` |

- ⚠️ **Olvidar la `f`** hace que se imprima `{nombre}` tal cual. Error muy típico.
- `:.2f` solo cambia lo que se **ve**, no el número guardado.

## 4. Operadores aritméticos

| Símbolo | Qué hace | Ejemplo |
|---|---|---|
| `+` `-` `*` | sumar, restar, multiplicar | `3 * 4` → `12` |
| `/` | dividir (da decimales) | `7 / 2` → `3.5` |
| `//` | dividir y quedarse con la parte entera | `7 // 2` → `3` |
| `%` | **resto** de la división | `7 % 2` → `1` |
| `**` | elevar a una potencia | `2 ** 3` → `8` |
| `abs(x)` | quitar el signo (valor absoluto) | `abs(-5)` → `5` |

- Truco del resto: `n % 2 == 0` → `n` es par. `n % d == 0` → `n` es múltiplo de `d` (se puede dividir justo).
- `//` y `%` sirven para trocear: `125 // 60` = 2 horas, `125 % 60` = 5 minutos sobrantes.
- Dividir entre 0 → `ZeroDivisionError`.
- Si el ejercicio dice "sin el operador de potencia", se usa un bucle (ver [receta del acumulador](#11-patrones-habituales)).

## 5. Condicionales: if, elif, else

```python
if nota >= 5:
    print("Aprobado")
elif nota >= 4:
    print("Casi")
else:
    print("Suspenso")
```

- Los **dos puntos** `:` y la **sangría** (4 espacios) son obligatorios.
- Se mira de arriba abajo y **solo se ejecuta el primer bloque que cumple**. Los demás se saltan.
- `elif` y `else` son opcionales. `else` no lleva condición: recoge "todo lo demás".
- Dentro de un `if` caben más `if`.

## 6. Operadores de comparación y lógicos

| Símbolo | Significa |
|---|---|
| `==` | igual (¡dos signos!; uno solo es asignar) |
| `!=` | distinto |
| `<` `>` `<=` `>=` | menor, mayor, menor o igual, mayor o igual |

| Palabra | Cuándo es verdadero | Ejemplo |
|---|---|---|
| `and` | **las dos** condiciones | `x > 0 and x < 10` |
| `or` | **al menos una** | `x < 1 or x > 10` |
| `not` | lo contrario | `not hecho` |
| `in` | está dentro de un grupo | `letra in "aeiou"` |

- Rango válido: `1 <= x <= 10`, o con `and`. Rango **inválido**: `x < 1 or x > 10`.
- Cada lado de `and`/`or` necesita su comparación completa: `x == 1 or x == 2`, **no** `x == 1 or 2`.

## 7. Variables booleanas (banderas)

Una bandera es una variable `True`/`False` que recuerda si algo ocurrió.

```python
encontrado = False          # al principio: "aún no"
if numero == objetivo:
    encontrado = True       # "ya ha pasado"

if encontrado:              # NO hace falta "== True"
    print("Hallado")
if not encontrado:
    print("No hallado")
```

- Una vez en `True`, **no se vuelve a poner en `False`** dentro del mismo recorrido.
- Se escribe `if bandera:`, no `if bandera == True:`.

## 8. Bucle for

Cuando **se sabe cuántas vueltas** o hay un rango.

```python
for i in range(1, 6):
    print(i)        # 1 2 3 4 5
```

- `range(inicio, fin)`: **el final no entra.** Para llegar al 5 hay que poner 6. Por eso se escribe `range(1, n + 1)`.
- `range(5)` equivale a `range(0, 5)`: 0, 1, 2, 3, 4.
- `range(a, b, 2)`: salta de 2 en 2.
- `i` es una variable que cambia sola en cada vuelta. Todo lo que está **con sangría** debajo del `for` es lo que se repite.

## 9. Bucle while

Cuando **no se sabe cuántas vueltas**: "mientras pase esto, repite".

```python
numero = 1
while numero <= 3:
    print(numero)
    numero = numero + 1     # ¡imprescindible!
```

- La condición se mira **al empezar cada vuelta**, no a mitad.
- **Bucle colgado = una variable de la condición que nunca cambia.** Revisar la sangría: si el `numero = numero + 1` quedó dentro de un `if`, a veces no se ejecuta.
- **Lectura adelantada** (pedir datos hasta una señal de parada, p. ej. el 0): se pide **antes** del bucle, se procesa dentro y se vuelve a pedir **al final**.

```python
numero = int(input("Número (0 para acabar): "))
while numero != 0:
    # ...procesar numero...
    numero = int(input("Número (0 para acabar): "))
```

- Es necesario porque la condición se mira al empezar: la señal de parada **no debe procesarse** como si fuera un dato.
- `break` sale del bucle al instante; `continue` salta a la vuelta siguiente.

## 10. Elección entre for y while

| Pregunta | Respuesta |
|---|---|
| ¿Sé cuántas vueltas? ¿Hay un rango? | `for` |
| ¿Repite hasta que ocurra algo? | `while` |
| ¿Hay un tope de intentos **y** una salida anticipada? | `while` con varias condiciones (`and`) |

- **El dato del usuario puede ser un valor o un tope.** "Introduce el exponente 3": ¿se usa como un número o como *las veces que se repite algo*? Si es lo segundo, es el tope del bucle (`range(exponente)` o `while contador < exponente`).
- Para **repetir** → bucle. Para **decidir** → `if`. Se combinan: un `if` dentro de un bucle.

## 11. Patrones habituales

**Acumulador** (sumar o multiplicar muchas cosas). Se crea **antes** del bucle:

```python
total = 0                    # para SUMAR se empieza en 0
for n in range(1, 6):
    total = total + n        # 1+2+3+4+5 = 15

factorial = 1                # para MULTIPLICAR se empieza en 1
for n in range(1, 6):
    factorial = factorial * n   # 1*2*3*4*5 = 120
```

> Empezar un producto en 0 lo deja siempre en 0.

**Contador** (cuántas veces pasa algo):

```python
positivos = 0
if numero > 0:
    positivos = positivos + 1
```

**Media**: `suma / cantidad`. Con cantidad 0 → error; comprobar antes con un `if`.

**Mayor / menor**: se arranca con el primer dato y se compara con cada nuevo.

```python
mayor = primero
if nuevo > mayor:
    mayor = nuevo
```

**Variable que cambia sola** (p. ej. un pago que se duplica cada mes): se usa, y **después** se actualiza.

```python
pago = 10
for mes in range(1, 4):
    print(pago)            # 10, 20, 40
    pago = pago * 2        # actualizar AL FINAL
```

**¿Es primo?** (no es divisible por nada entre 2 y su raíz cuadrada)

```python
es_primo = True
divisor = 2
while divisor * divisor <= numero:
    if numero % divisor == 0:
        es_primo = False
    divisor = divisor + 1    # al nivel del while, NO dentro del if
```

> `divisor * divisor <= numero` equivale a "hasta la raíz cuadrada", sin necesidad de calcularla. Con el 1 o el 0 hay que tratarlos aparte.

**Potencia sin `**`**: multiplicar la base tantas veces como diga el exponente.

```python
resultado = 1
for vuelta in range(exponente):
    resultado = resultado * base
```

**Exponente negativo**: calcular con el exponente sin signo (`abs`) y al final hacer `1 / resultado`. Base 0 con exponente negativo es dividir entre 0: comprobarlo antes.

**Tabla de multiplicar**: un `for` del 1 al 10 y `print(f"{n} x {i} = {n * i}")`.

**Validar una entrada** (repetir hasta que sea válida):

```python
numero = int(input("Número del 1 al 10: "))
while numero < 1 or numero > 10:
    numero = int(input("Inválido. Número del 1 al 10: "))
```

**Menú**: `while opcion != 5:` con el menú, el `input` y un `if/elif/else` dentro. El número de salida debe coincidir en el `while` y en el `elif`.

## 12. Bucles anidados

El de dentro da **todas** sus vueltas por cada vuelta del de fuera (como un reloj: 60 segundos por cada minuto).

```python
for trabajador in range(1, 4):
    horas = 0                         # se reinicia por trabajador
    for dia in range(1, 6):
        horas = horas + float(input("Horas: "))
    print(f"Trabajador {trabajador}: {horas} h")
```

**Regla de oro:** cada variable se crea (o se pone a cero) **en el nivel donde empieza su cuenta**.

| Cuenta de... | Se reinicia... |
|---|---|
| cada trabajador | dentro del bucle de trabajadores, antes del de días |
| toda la empresa | una sola vez, antes de todo |

## 13. Cadenas de texto (strings)

```python
frase = "Hola Mundo"
len(frase)            # 10 (cuenta los caracteres, espacios incluidos)
frase.lower()         # "hola mundo"
frase[:1]             # "H" (la primera letra)
"o" in frase          # True
```

- `"a" in "aeiou"` sirve para comprobar si una letra es vocal.
- Con tildes o mayúsculas: pasar a minúsculas con `.lower()` y añadir las vocales con tilde a la lista. `len()` ayuda a comprobar que el usuario escribió **una** sola letra.
- Si se pulsa solo Enter, `input` devuelve `""` (texto vacío, `len` = 0).

## 14. Módulos random y time

Los `import` van **arriba del todo**.

```python
import random
secreto = random.randint(1, 100)   # entero entre 1 y 100, AMBOS incluidos

import time
time.sleep(1)                       # pausa de 1 segundo
```

## 15. Errores frecuentes

| Qué se ve | Qué pasa | Qué hacer |
|---|---|---|
| `ValueError` | `int()` o `float()` recibió algo que no es un número (una letra, vacío) | Escribir un número. Se podrá controlar con excepciones más adelante |
| `ZeroDivisionError` | Se dividió entre 0 | Comprobar con un `if` antes |
| `NameError` | Variable que no existe (casi siempre por una errata) | Revisar la ortografía del nombre |
| `IndentationError` | Sangría mal | Alinear con 4 espacios; no mezclar tabuladores |
| `SyntaxError` | Falta un `:`, comillas o paréntesis | Mirar la línea que indica (o la anterior) |
| `TypeError` | Se mezcló texto con número (p. ej. sin `int()`) | Convertir el `input` |
| El programa no acaba | Bucle infinito | Ctrl + C y revisar qué variable de la condición no cambia |
| Sale `{variable}` en pantalla | Falta la `f` del f-string | Añadir `f` antes de las comillas |
| Falta el último elemento | `range` no incluye el final | Sumar 1 al final |
| Una vuelta de más o de menos | `<` frente a `<=` | Probar con un caso pequeño a mano |

## 16. Lista de verificación antes de entregar

- [ ] **Leer el enunciado entero**, hasta la última línea (a veces dice "entero positivo", "sin usar...", "hasta que...").
- [ ] Probar con datos **"no bonitos"** (decimales, números raros), no solo con 10 o 100 que esconden fallos.
- [ ] Probar los **extremos**: el 0, el 1, el primero y el último, un negativo.
- [ ] Si algo no se entiende, **escribir la suposición en un comentario** en el propio fichero.
- [ ] Un ejercicio muy largo se trocea: primero el esqueleto del bucle, luego lo de dentro, y se prueba en cada paso.
- [ ] Cuando un programa da un resultado raro: **simular a mano** unas vueltas, apuntando los valores de cada variable en una tabla.
- [ ] Rama `ejercicio_N` nueva desde `main`, con un único fichero `ejercicio_N.py`. Las mejoras posteriores van en commits nuevos de la misma rama.

---

*Regla final: si algo no se entiende en unos minutos, no pasa nada por pedir la solución comentada y entenderla pieza a pieza. Hasta los monos aprenden a pelar plátanos mirando a otro mono.* 🐒🍌
