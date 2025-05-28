def impares(n):
    if not n > 10:
        raise ValueError("El número debe ser mayor a 10")
    lista = []
    for i in range(2, n + 1):
        if i % 2 != 0:
            lista.append(i)
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
