# tomar captura de las dos excepciones y explicarlo en el documento

""" 
numero = int(input("Introduce un número: "))
resultado = 10 / numero

print("Resultado:", resultado) """

# documentar que ahora estamos poniendo un mensaje para las excepciones


try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero

    print("Resultado:", resultado)

except ValueError:
    print("Error: Se ingresón algo que no es un número entero.")
except ZeroDivisionError:
    print("Error: No se puede dividir entre 0.")
