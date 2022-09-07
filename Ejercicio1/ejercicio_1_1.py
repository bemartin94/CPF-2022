def pluralize(lista):
    lista2 = []
    for item in lista:
        if item not in lista2:
            lista2.append(item)
        else:
            lista2.append(item + "s")
            lista2.remove(item)
            lista.remove(item)
    return lista2
