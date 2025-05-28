import re as expresiones_regulares

# Función que valida y retorna la frase formateada
def validar_frase(frase):
    frase_formateada = frase.lower().replace(" ", "")
    
    if frase_formateada.strip() == "":
        raise ValueError("La frase no puede estar vacía.")
    
    # usamos una expresión regular para validar que haya letras en la frase
    if not expresiones_regulares.search(r"[a-zA-Z]", frase_formateada):
        raise ValueError("La frase debe tener carácteres válidos.")
    
    return frase_formateada

# Función para validar y retornar la frase formateada
def validar_letra(letra):
    letra_formateada = letra.lower()
    if not len(letra_formateada) == 1:
        raise ValueError("Debe ser solo una letra")
    if not letra_formateada.isalpha():
        raise ValueError("La letra debe ser un carácter del abecedario")
    
    return letra_formateada

# Función que cuenta las ocurrencias de una letra en una frase
def contar_letra(frase, letra):   
    # inicializamos las ocurrencias en 0 
    ocurrencias = 0
    # y dado que los strings son iterables, vamos carácter por carácter
    # si el carácter es igual a la letra buscada, se incrementa la ocurrencia en 1
    for i in frase:
        if (i == letra):
            ocurrencias += 1
    return ocurrencias

while True:
    try:
        frase = input("Introduce una frase: ")
        frase_formateada = validar_frase(frase)
        letra = input("Introduce una letra: ")
        letra_formateada = validar_letra(letra)

        ocurrencias = contar_letra(frase_formateada, letra_formateada)
        print(f"La letra {letra_formateada} aparece {ocurrencias} veces.")
    except ValueError as e:
        print(f"Error: {e}")

    salida = input("Ingresa cualquier valor para continuar, 0 para salir: ")
    if salida == "0":
        break
print("----------FIN DEL PROGRAMA----------")



    
