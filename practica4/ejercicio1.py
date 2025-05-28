# Función que retorna la lista con todos los impares
def impares(n):
    # validar que el número es mayor a 10
    if not n > 10:
        raise ValueError("El número debe ser mayor a 10")
    
    # se crea la lista, y recorremos todos los números hasta n
    # si son impares, se añaden a la lista
    lista = []
    for i in range(2, n + 1):
        if i % 2 != 0:
            lista.append(i)
    
    # finalmente retornamos la lista
    return lista


while True:
    try:
        limite = int(input("Ingresa un número MAYOR a 10: "))
        print(impares(limite))
    except ValueError as e:
        print(f"Error: {e}")
    
    salida = input("Ingresa cualquier valor para continuar, 0 para salir: ")
    if salida == "0":
        break
print("----------FIN DEL PROGRAMA----------")
