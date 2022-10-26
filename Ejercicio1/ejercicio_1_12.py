# Function to create combinations
# without itertools
def combinaciones(lst, n):
    if n == 0:
        return [[]]

    l = []
    for i in range(0, len(lst)):

        m = lst[i]
        remLst = lst[i + 1:]

        remainlst_combo = combinaciones(remLst, n - 1)
        for p in remainlst_combo:
            l.append([m, *p])

    return l

lista= ["a","b","c","d","e","f"]
print(combinaciones(lista, 4))