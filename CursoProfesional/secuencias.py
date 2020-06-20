"""
curso = "curso de python 3"

resultado = curso[1:16:2]
curso[0] = "C"
print(resultado)
"""

lenguajes = "Python; Java; Ruby; PHP; Swift; JavaScript; C#; C; C++"
separador = ";"
resultado = lenguajes.isplit(separador) #Resultado es una lista
nuevo_string = separador.join(resultado)
print(resultado)
print(nuevo_string)