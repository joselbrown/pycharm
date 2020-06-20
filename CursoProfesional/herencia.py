class Animal:
    def comer(self):
        print("Comiendo")
    def dormir(self):
        print("Durmiendo")

class Perro(Animal):
    def __init__(self,nombre):
        self.nombre = nombre
    def ladrar(self):
        print("Ladrando")
firulais = Perro("Firulais")
firulais.ladrar()
firulais.comer()
firulais.dormir()