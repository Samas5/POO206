def es_biciesto(year):
    # No existen años negativos ni 0
    if year <= 0:
        raise ValueError("Año NO válido")
    # Un año es biciesto si es divisible entre 4 y no entre 100, o si es divisible entre 400]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

while True:
    try:
        entrada = input("Ingresa un año: ")
        # Esta función se asegura de que todo lo contenido en un string son solo números enteros
        if not entrada.isdigit():
            raise ValueError("Debes ingresar un año en formato numérico ENTERO.")
        # Una vez validado, se hace el casting a int
        year = int(entrada)
        # Se valida con la función
        if es_biciesto(year):
            print("El año es biciesto")
        else:
            print("El año NO es biciesto")
    # as sirve para asignar un alias a algo, lo uso aquí porque tengo dos mensajes diferentes para ValueError, y este es dinámico
    except ValueError as e:
        print(f"ERROR: {e}")

    salida = input("Ingresa cualquier valor para continuar, 0 para salir: ")
    if salida == "0":
        break
print("----------FIN DEL PROGRAMA----------")
