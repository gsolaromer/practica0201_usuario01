# Solicitar el número de teléfono
numero_telefono = input("Por favor, ingresa un número de teléfono con el formato +34-XXXXXXXXX-XX: ")

# Verificar que el formato del número sea válido
if numero_telefono.startswith("+34-") and len(numero_telefono) == 15 and numero_telefono[9] == '-':
    # Extraer el número central (sin el prefijo ni la extensión)
    numero_central = numero_telefono[4:13]
    print("Número central del teléfono:", numero_central)
else:
    print("El número de teléfono no tiene el formato válido (+34-XXXXXXXXX-XX).")