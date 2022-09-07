def operacion_aritmetica(operacion):
    factores = list(operacion.split(" "))
    if factores[1] == "+":
        return int(factores[0]) + int(factores[2])
    if factores[1] == "-":
        return int(factores[0]) - int(factores[2])
    if factores[1] == "//":
        if factores[2] == "0":
            return "No se puede dividir por 0"
        else:
            return int(factores[0]) // int(factores[2])
    if factores[1] == "*":
        return int(factores[0]) * int(factores[2])
