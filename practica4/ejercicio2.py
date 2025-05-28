# Función que retorna la lista con cuenta hacia atrás desde n hasta 0
def cuenta_atras(n):
    # error si n es menor que cero, para impedir números negativos
    if n < 0:
        raise ValueError("El número debe ser entero positivo.")
    lista = []
    # añadimos a la lista todos los números desde 0 hasta n
    for i in range(0, n + 1):
        lista.append(i)

    # y la retornamos invertida
    return lista[::-1]

while True:
    try:
        x = int(input("Ingresa un número entero positivo: "))
        print(cuenta_atras(x))
    except ValueError as e:
        print(f"Error: {e}")

    salida = input("Ingresa cualquier valor para continuar, 0 para salir: ")
    if salida == "0":
        break
print("----------FIN DEL PROGRAMA----------")