# Solicitar información del producto
nombre_producto = input("Por favor, ingresa el nombre del producto: ")
precio_unitario = float(input("Ingresa el precio unitario del producto: "))
numero_unidades = int(input("Ingresa el número de unidades: "))

# Calcular el costo total
coste_total = precio_unitario * numero_unidades

# Formatear la cadena de salida
cadena_salida = f"{nombre_producto}: {precio_unitario:.2f} {numero_unidades:03d} {coste_total:.2f}"

# Mostrar la cadena formateada
print(cadena_salida)