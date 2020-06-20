def comenzar_play_list(lista):
    def reproducir():
        for val in lista:
            print(val)


reproducir()
print(lista)
lista = ["track 1", "track 2", "track 3", "track 4"]
comenzar_play_list(lista)