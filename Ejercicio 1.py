# Solicitar el nombre del usuario y el número de repeticiones
nombre_usuario = input("Por favor, ingresa tu nombre: ")
numero_repeticiones = input("Ingresa un número entero: ")

# Verificar si el número ingresado es un entero válido
if numero_repeticiones.isdigit():
    numero_repeticiones = int(numero_repeticiones)
    
    # Imprimir el nombre del usuario tantas veces como el número introducido
    output = f"{nombre_usuario}\n" * numero_repeticiones
    print(output)
else:
    print("El número ingresado no es válido. Debe ser un número entero.")