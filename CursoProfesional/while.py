""""
diccionario ={'a':1, 'b':2}
for llave in diccionario:
    print(llave)

valores = ((10, 20), ["strings", "strings"], (True, False))
for valor1, valor2 in valores:
    print(valor1,valor2)

titulo = "Curso de Python 3"
for caracter in titulo:
    if not "y" != caracter:
        continue
    print(caracter)
"""
calificacion = int(input("Pon la nota: "))
color = "verde" if calificacion >= 7 else "rojo"
print(calificacion, color)

