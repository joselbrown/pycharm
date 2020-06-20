class Animal:
    def comer(self):
        print("Comiendo")
    def dormir(self):
        print("Durmiendo")

    class Mascota:

    class Perro(Animal, Mascota):
         def __init__(self,nombre):
            self.nombre = nombre
         def ladrar(self):
            print("Ladrando")
          def dormir(self):
        print(self.nombre, "Esta durmiendo ")
firulais = Perro("Firulais")
firulais.dormir()