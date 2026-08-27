from collections import deque


def ventana_deslizante(iterable, tamano=3):
    ventana = deque(maxlen=tamano)
    for elemento in iterable:
        ventana.append(elemento)
        if len(ventana) == tamano:
            yield tuple(ventana)

def main():
    print(list(ventana_deslizante([1, 2, 3, 4, 5], 3)))
    print(list(ventana_deslizante([1, 2, 3, 4, 5], 2)))

if __name__ == "__main__":
    main()