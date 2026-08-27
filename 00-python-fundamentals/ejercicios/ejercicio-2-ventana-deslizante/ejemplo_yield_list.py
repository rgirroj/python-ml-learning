def contador():
    print("Antes del primer yield")
    yield 1
    print("Antes del segundo yield")
    yield 2
    print("Antes del tercer yield")
    yield 3
    print("Se acabó, la función termina")

def main():
    resultado = []
    g = contador()
    while True:  # este bible equivaldría a list(contador())
        try:
            valor = next(g)
            resultado.append(valor)
        except StopIteration:
            break
    print(resultado)


if __name__ == "__main__":
    main()