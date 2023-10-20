# Solicitar el precio del producto en euros con dos decimales
precio = input("Por favor, introduce el precio del producto en euros (con dos decimales): ")

# Verificar si el valor ingresado tiene el formato correcto
if precio.count('.') == 1:
    euros_str, centimos_str = precio.split('.')
    
    # Convertir las partes a enteros
    euros = int(euros_str)
    centimos = int(centimos_str)
    
    # Mostrar el número de euros y céntimos
    print(f"{euros} euros y {centimos} céntimos")
else:
    print("El valor introducido no tiene el formato correcto (por ejemplo, 10.50).")