import sys

precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("<umbral> [mayor|menor]")
    sys.exit(1)

try:
    umbral = int(sys.argv[1])
except ValueError:
    print("Error: El umbral debe ser un número entero.")
    sys.exit(1)

filtro = "mayor" if len(sys.argv) == 2 else sys.argv[2]

if filtro == "mayor":
    productos_filtrados = [producto for producto, precio in precios.items() if precio > umbral]
    print(f"Los productos mayores al umbral son: {', '.join(productos_filtrados)}")
elif filtro == "menor":
    productos_filtrados = [producto for producto, precio in precios.items() if precio < umbral]
    print(f"Los productos menores al umbral son: {', '.join(productos_filtrados)}")
else:
    print("Lo sentimos, no es una operación válida.")


