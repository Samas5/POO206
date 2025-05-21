# Intentamos ejecutar código que puede lanzar más de una excepción
try:
    # Pedimos al usuario que ingrese un número (puede fallar si mete texto)
    numero = int(input("Introduce un número: "))
    # Intentamos dividir 10 entre ese número (puede fallar si mete un cero)
    resultado = 10 / numero
# Capturamos dos tipos de errores posibles: ValueError y ZeroDivisionError
except (ValueError, ZeroDivisionError) as e:
    # Mostramos el mensaje de la excepción ocurrida
    print(f"Ocurrió un error: {e}")
