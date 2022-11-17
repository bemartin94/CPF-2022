class Carta:
    def __init__(self, figura, numero):
        self.figura = figura
        self.numero = numero

    def __str__(self):
        return "{},{}".format(self.figura, self.numero)

    def es_1_de_oro(self):
        return self.figura == "oro" and self.numero == 1

    def get_figura(self):
        return self.figura

    def get_numero(self):
        return self.numero