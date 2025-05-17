# 1. Comentarios

# Comentario de una sola línea

""" Comentario 
    de múltiples
    líneas
"""

# 2. Strings
""" print("Hola soy una cadena 🦍")
print("yo soy otra cadena") """

cadena = "hola, soy una cadena"
print(len(cadena))
print(cadena[2:5])
print(cadena[2:])
print(cadena[:5])

# 3. Variables
# Nunca poner un numero al inicio
# ESTO ESTA MAL ---> 234dk = "adios"
# investigar zip

x = "samael"
x = int(3)
y = float(3)
z = str(3)
print(x, y, z)
print(type(x))

# 4. Solicitud de datos

a = input("Introduce cualquier dato: ")
b = int(input("Introduce un número entero: "))
c = float(input("Introduce un número decimal: "))

print(a, b, c)

# Boolean, comparación y lógicos 
# comparación:
print(10 > 9)
print(10 < 9)
print(10 == 9)
print(10 >= 9)
print(10 <= 9)
print(10 != 9)

# lógicos:
x = 1
print(x < 5 and x < 10)
print(x < 5 or x < 10)
print(not(x < 5 and x < 10))
