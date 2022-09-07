
def square_digits(numero):
    cuadrados = []
    for digito in str(numero):
       cuadrados.append(str(int(digito)*int(digito)))
    resultado = "".join(cuadrados)
    return resultado


