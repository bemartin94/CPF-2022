class Lampara:
    def __init__(self, prendida = True):
        self.prendida = prendida

    def esta_prendida(self):
        return self.prendida

    def apagar(self):
        if self.prendida:
            self.prendida = False

    def prender(self):
        if not self.prendida:
            self.prendida = True

    def alternar(self):
        self.prendida = not(self.prendida)

    def get_esta_prendida_str(self):
        if self.prendida:
            return("PRENDIDA")
        else:
            return("APAGADA")

