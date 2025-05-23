# Función que recibirá un texto, idealmente YA FORMATEADO, para saber si es un palíndromo o no.
def es_palindromo(texto):
    # isalpha() devuelve true si no hay letras en un string, lo negamos para lanzar el error con not
    if not texto.isalpha():
        raise ValueError("Debes ingresar texto")
    # Importantísimo slice operator con -1 para invertir un string
    if (texto == texto[::-1]):
        return True
    else:
        return False

try:
    # Formateamos el texto, quitamos los espacios y bajamos todo a minusculas
    texto = input("Ingresa un texto: ").replace(" ", "").lower()
    if (es_palindromo(texto)):
        print("Es palíndromo")
    else:
        print("NO es palíndromo")

# Lanzamos el error si lo que se ingresó no es un número
except ValueError as e:
    print(f"Error: {e}")
