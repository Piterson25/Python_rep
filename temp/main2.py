def split(napis, separator):
    lista = []
    word = ''
    for znak in napis:
        if znak not in separator:
            word += znak
        elif word:
            lista.append(word)
            word = ''

    if word:
        lista.append(word)

    return lista
