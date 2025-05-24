# Bucle para estar ciclando y probar el error
while True:
    try:
        # Si se ingresa algo diferente a un número entero, fallará el castinf del int y aquí saldra el ValueError
        num = int(input("Ingresa un número: "))
        if num % 2 == 0:
            print("El número es par")
        else:
            print("El número es impar")
        # Aquí lo manejamos
    except ValueError:
        print("ERROR: Ingresa un número válido")
    
    salida = input("Ingresa cualquier valor para continuar, 0 para salir: ")
    if salida == "0":
        break
print("----------FIN DEL PROGRAMA----------")
