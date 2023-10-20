# Solicitar la fecha de nacimiento en formato dd/mm/aaaa
fecha_nacimiento = input("Por favor, introduce tu fecha de nacimiento en formato dd/mm/aaaa: ")

# Separar la fecha en día, mes y año
partes_fecha = fecha_nacimiento.split('/')

# Verificar y ajustar la longitud del día y el mes
dia = partes_fecha[0]
mes = partes_fecha[1]
año = partes_fecha[2]

if len(dia) == 1:
    dia = "0" + dia

if len(mes) == 1:
    mes = "0" + mes

# Mostrar la fecha de nacimiento con el formato correcto
print(f"Día: {dia}")
print(f"Mes: {mes}")
print(f"Año: {año}")