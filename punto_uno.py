def inverso(lista):
    if len(lista) == 0:
        return 0

    else:
        inverso(lista[1:])
        print(lista[0])

mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("lista inversa")
inverso(mi_lista)