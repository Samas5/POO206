# Intentamos abrir un archivo y leer su contenido
try:
    # Abrimos el archivo "datos.txt" en modo de solo lectura
    archivo = open("datos.txt", "r")
    # Leemos todo el contenido del archivo
    contenido = archivo.read()
    # Imprimimos el contenido leído
    print(contenido)
# Capturamos el error si el archivo no se encuentra
except FileNotFoundError:
    # Mostramos un mensaje indicando que no existe el archivo
    print("El archivo no existe.")
# Este bloque siempre se ejecuta, haya ocurrido o no ocurrido el error
finally:
    print("Este bloque siempre se ejecuta.")
