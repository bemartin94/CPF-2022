def unique_sort(lista):
    lista2 = []
    for item in lista:
        if item not in lista2:
            lista2.append(item)
        else:
            lista2.append(item)
            lista2.remove(item)
            lista.remove(item)
    return sorted(lista2)

print(unique_sort([6, 7, 3, 2, 1]))