def crear_mensajes(nombre):
    mensaje = "Hola {}, bienvenido al curso de python 3".format(nombre)
    return mensaje
nuevo_mensaje = crear_mensajes("Eduardo")
print(nuevo_mensaje)