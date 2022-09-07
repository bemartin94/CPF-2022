def simon_says(lista1, lista2):
    lista2.pop(0)
    lista2.append((lista2[-1])+1)
    return lista1 == lista2
