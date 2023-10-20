# Solicitar el correo electrónico del usuario
correo_usuario = input("Por favor, ingresa tu correo electrónico: ")

# Separar el correo en nombre de usuario y dominio
nombre_usuario, dominio = correo_usuario.split('@')

# Crear un nuevo correo con el dominio "ceu.es"
nuevo_correo = f"{nombre_usuario}@ceu.es"

# Mostrar el nuevo correo electrónico
print("Nuevo correo electrónico con dominio ceu.es:", nuevo_correo)