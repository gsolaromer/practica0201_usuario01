# Solicitar al usuario que introduzca una frase
frase = input("Por favor, introduce una frase: ")

# Solicitar al usuario que introduzca una vocal
vocal = input("Introduce una vocal: ")

# Verificar que la entrada sea una vocal válida
if vocal in "aeiouAEIOU":
    # Reemplazar la vocal en la frase con la vocal en mayúscula
    frase_modificada = frase.replace(vocal, vocal.upper())

    # Mostrar la frase modificada
    print("Frase con la vocal en mayúscula:", frase_modificada)
else:
    print("La entrada no es una vocal válida.")