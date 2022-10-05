
class Juego:
    def __init__(self, jugadores, mazo):
        self.jugadores = jugadores
        self.mazo = mazo

    def iniciar(self, mazo, jugador, carta):
        mazo.mezclar(self)
        while len(self.jugadores) > 1:
            carta = jugador.tomar_carta(mazo)
            if carta.es_1_de_oro():
                self.eliminar_jugador()
            else

    def ronda(self):
        while not

    def finalizado(self):
        return len(self.jugadores) < 1

    def get_ganador(self):
        pass

    def eliminar_jugador(self,carta,jugador):
        if carta.es_1_de_oro():
            self.remove()
