def sevenBoom(array):
    lista_boom= []
    for x in array:
        if "7" in str(x):
            lista_boom.append(x)

    if len(lista_boom):
        return "Boom!"
    else:
        return "No se encuentra el número 7 en el array"


