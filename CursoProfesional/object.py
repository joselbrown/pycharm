class Gato:
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self):
        return self.nombre
class Pato(object):
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self):
        return self.nombre
gato  = Gato("Bigotes")
pato = Pato("Baki")

print(gato.__dict__)
print(pato.__dict__)