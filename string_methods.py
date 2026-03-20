def string_methods():
    """Demuestra el uso de métodos de string: strip, lstrip, rstrip, upper, lower,
    title, find, replace, count, operador in, slicing con paso, reverso,
    f-strings y strings multilínea.
    1. `nombre` sin espacios (strip), sin espacios a la izquierda (lstrip), sin espacios a la derecha (rstrip).
    2. `frase` en mayúsculas, minúsculas y formato título.
    3. Imprimir la posición de `"gran"` en `frase`.
    4. `frase` reemplazando `"programacion"` por `"desarrollo"`.
    5. Contar la cantidad de `'a'` en `frase`.
    6. Verificar si `"Python"` y `"Java"` están en `frase`.
    7. Extraer `"Python"` de `frase` usando slicing.
    8. Caracteres no contiguos de `"Python"` con paso 2.
    9. `"Python"` en orden inverso.
    10. Combinar `nombre` (sin espacios) y `"Python"` en un f-string.
    11. Imprimir el string multilínea.

    **Salida esperada:**

    ```
    Strip: Grace Hopper
    Lstrip: Grace Hopper   
    Rstrip:    Grace Hopper
    Upper: PYTHON ES UN GRAN LENGUAJE DE PROGRAMACION
    Lower: python es un gran lenguaje de programacion
    Title: Python Es Un Gran Lenguaje De Programacion
    Find: 13
    Replace: Python es un gran lenguaje de desarrollo
    Count: 4
    Contiene Python: True
    Contiene Java: False
    Slice: Python
    Paso: Pto
    Reverso: nohtyP
    Formato: Grace Hopper sabe Python
    Linea 1
    Linea 2
    Linea 3

    """
    nombre = "   Grace Hopper   "
    frase = "Python es un gran lenguaje de programacion"
    multilinea ="""Linea 1\nLinea 2\nLinea 3"""

    print(f"Strip: {nombre.strip()}")
    print(f"Lstrip: {nombre.lstrip()}")
    print(f"Rstrip: {nombre.rstrip()}")
    print(f"Upper: {frase.upper()}")
    print(f"Lower: {frase.lower()}")
    print(f"Title: {frase.title()}")
    print(f"Find: {frase.find("gran")}")
    print(f"Replace: {frase.replace("programacion", "desarrollo")}")
    print(f"Count: {frase.count('a')}")
    print(f"Contiene Python: {"Python" in frase}")
    print(f"Contiene Java: {"Java" in frase}")
    print(f"Slice: {frase[:6]}")
    print(f"Paso: {frase[:6:2]}")
    print(f"Reverso: {frase[5::-1]}")
    print(f"Formato: {nombre.strip()} sabe {frase[:6]}")
    print(multilinea)

string_methods()