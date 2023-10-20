# Solicitar los productos de la cesta de compra separados por comas
productos = input("Por favor, introduce los productos de tu cesta de compra separados por comas: ")

# Dividir los productos en una lista
lista_productos = productos.split(',')

# Mostrar cada producto en una línea distinta
for producto in lista_productos:
    print(producto.strip())  # strip() elimina espacios en blanco alrededor del producto si los hay