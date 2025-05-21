# Definimos una función para dividir dos números
def dividir(a, b):
    # Verificamos si el divisor es cero
    if b == 0:
        # Si es cero, lanzamos una excepción del tipo ValueError con un mensaje personalizado
        raise ValueError("No se puede dividir entre cero.")
    # Si no hay problema, se realiza la división
    return a / b

# Intentamos usar la función dividir dentro de un bloque try
try:
    # Esto causará un error porque estamos dividiendo entre cero
    print(dividir(10, 0))
# Capturamos el error específico ValueError y lo nombramos como 'e'
except ValueError as e:
    # Mostramos el mensaje del error capturado
    print(f"Error capturado: {e}")
