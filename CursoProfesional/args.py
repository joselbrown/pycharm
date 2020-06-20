def suma(*args):
    total = 0
    for valor in args:
        total+=valor
        return  total

resultado  = suma (10, 20 , 30, 40, 50, 60, 70)
print(resultado)