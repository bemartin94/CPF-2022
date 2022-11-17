class Carta:
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor

class Baraja:
    def __init__(self):
        self.cartas = self.generar_mazo()

    def generar_mazo(self):
        mazo=[]
        palos=["oro", "espada", "basto", "copa"]
        for palo in palos:
            for numero in range(1,13):
                mazo.append(Carta(palo, numero))
        return mazo

