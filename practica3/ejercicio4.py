# Módulo para trabajar con expresiones regulares, básicamente patrones que nos permiten encontrar coincidencias en strings
import re as expresiones_regulares

# Función que recibe la contraseña y la valida
def validar_password(password):
    if len(password) < 10:
        raise ValueError("Contraseña demasiado corta.")
    # la función search (del módulo expresiones regulares) recibe dos argumenmtos: la expresión regular y el string donde se buscará
    # r sirve para que el caracter de escape se desactive y sea considerado texto normal
    # la expresión \d busca un dígito numérico en el string 
    if not expresiones_regulares.search(r"\d", password):
        raise ValueError("Debe contener al menos un número")
    # la expresión [^a-zA-Z0-9] busca cualquier carácter que NO sea una letra mayúscula, minúscula ni un número
    # es decir, busca al menos un carácter especial 
    if not expresiones_regulares.search(r"[^a-zA-Z0-9]", password):
        raise ValueError("Debe contener al menos un carácter especial.")
    
    return True

print("La contraseña debe contener al menos:\n- 10 carácteres\n- Un número\n- Un carácter especial")

while True:
    try:
        password = input("Ingresa una contraseña: ")
        # la contraseña ingresada se pasa a la función como argumento
        if validar_password(password):
            # y si es válida, imprime el mensajr
            print("Contraseña válida")
    except ValueError as e:
        print(f"Error: {e}")

    salida = input("Ingresa cualquier valor para continuar, 0 para salir: ")
    if salida == "0":
        break
print("----------FIN DEL PROGRAMA----------")
