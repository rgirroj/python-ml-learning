# operaciones.py

import math


def promedio(numeros: list[float]) -> float:
    if not numeros:
        raise ValueError("La lista no puede estar vacía")
    return sum(numeros) / len(numeros)

def desviacion_estandar(numeros: list[float]) -> float:
    if not numeros:
        raise ValueError("La lista no puede estar vacía")
    if len(numeros) == 1:
        raise ZeroDivisionError("La lista no puede sólo un elemento")

    media = promedio(numeros)
    n = len(numeros)
    return math.sqrt(sum((x - media) ** 2 for x in numeros)/(n-1))

