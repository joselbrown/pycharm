class Usuario:

    def __init__(self,username ="", correo="", nombre=""):
        self.username = " "
        self.correo = " "
        self.nombre = " "
    def saluda(self):
        print("Hola soy un usuario " + self.nombre)
    def mostrar_username(self):
        print(self.username)
    def mostrar_nombre(self):
        self.nombre
codi = Usuario("Codi", "codi@codigofacilito.com", "Codigo")
facilito = Usuario()

resultado = codi.saluda()
print(resultado)