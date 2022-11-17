class TableroDeBasquet:
    def __init__(self, local, visitante, puntos_local, puntos_visitante):
        self.local = local
        self.visitante =visitante
        self.puntos_local = puntos_local
        self.puntos_visitante = puntos_visitante

    def sumar3Puntos(self):
        self.puntos_local += 3
        self.puntos_visitante += 3

    def sumar2Puntos(self):
        self.puntos_local += 2
        self.puntos_visitante += 2

    def sumar1Punto(self):
        self.puntos_local += 1
        self.puntos_visitante += 1
