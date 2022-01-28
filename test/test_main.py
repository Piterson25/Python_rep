import main


def test_sort():
    lista = [5, 3, 3, 6, 7, 2, 1]
    assert main.bubble_sort(lista) == sorted(lista)
