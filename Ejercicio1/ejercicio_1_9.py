def get_budgets(lista_de_diccionarios):
    presupuestos_a_sumar = [x['budget'] for x in lista_de_diccionarios]
    return sum(presupuestos_a_sumar)
