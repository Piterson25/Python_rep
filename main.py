def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                x = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = x
    return lista




