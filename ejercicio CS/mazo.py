from carta import Carta
import random

class Mazo:
    def __init__(self):
        self.cartas = self.generar_mazo()

    def generar_mazo(self):
        mazo=[]
        palos=["oro", "espada", "basto", "copa"]
        for palo in palos:
            for numero in range(1,13):
                mazo.append(Carta(palo, numero))
        return mazo

    def mezclar_mazo(self):
        random.shuffle(self.cartas)

    def sacar_carta(self):
        carta_activa = self.cartas.pop()
        return carta_activa

    def reiniciar_mazo(self):
        Mazo.generar_mazo(self)

    def imprimir_mazo(self):
        for carta in self.cartas:
            print(carta)

nuevo_mazo= Mazo()
nuevo_mazo.mezclar_mazo()
nuevo_mazo.imprimir_mazo()