# main.py

def contar_palabras_largas(texto: str) -> dict[str, int]:
    palabras = texto.split()
    return {palabra: len(palabra) for palabra in palabras if len(palabra) > 4}


def main():
    texto = "el perro corre rapido por el parque enorme"
    resultado = contar_palabras_largas(texto)
    print(resultado)


if __name__ == "__main__":
    main()