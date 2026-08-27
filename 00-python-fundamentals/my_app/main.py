# main.py
import sys
from operaciones import promedio, desviacion_estandar

def main():
    numeros = [float(x) for x in sys.argv[1:]]
    try:
        resultado = promedio(numeros)
        print(f"El promedio es: {resultado:.2f}")
        desviacion = desviacion_estandar(numeros)
        print(f"La desviación es: {desviacion:.2f}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()