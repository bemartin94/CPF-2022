def same_length(string):
    lista = []
    lista_unos= []
    lista_ceros=[]
    a = string[0]
    for x in string[1:]:
        if (x != a[-1]):
            lista.append(a)
            a = x
        else:
            a += x
    lista.append(a)
    print(lista)

    for x in lista:
        if "1" in x:
            lista_unos.append(x)
        else:
            lista_ceros.append(x)

    if len(lista_unos) != len(lista_ceros):
        return False

    for x in range(len(lista_unos)):
        if not len(lista_unos[x]) == len(lista_ceros[x]):
            return False
    return True



