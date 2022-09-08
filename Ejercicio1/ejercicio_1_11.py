##acá la segunda prueba no funciona porque entendi mal la consigna
##REVISAR

def letrasMultiplicadas(letras, numero):
    lista_letras = []
    resultado_final = []
    a = letras[0]
    for x in letras[1:]:
        if (x != a[-1]):
            lista_letras.append(a)
            a = x
        else:
            a += x
    lista_letras.append(a)

    for letra in lista_letras:
        contador = numero
        while contador > 0:
            resultado_final.append(letra[0])
            contador -= 1

    return ''.join(resultado_final)