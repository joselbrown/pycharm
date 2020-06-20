class Circulo:
    pi = 3.14159265 #es una variable de clase
    def __init__(self,radio):
        self.radio = radio #radio es una variable  de instancia , son independientes de cada una de ellas.

circulo_a = Circulo(10)
circulo_b = Circulo(20)

circulo_b.radio = 100


print(circulo_a.pi)
print(circulo_b.pi)
