
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre

    def tomar_carta(self, mazo):
       mazo.sacar_carta()

