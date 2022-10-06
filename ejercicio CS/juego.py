
class Juego:
    def __init__(self, jugadores, mazo):
        self.jugadores = jugadores
        self.mazo = mazo

    def iniciar(self, mazo, indice):
        mazo.mezclar(self)
        while not self.finalizado:
            self.ronda(mazo, indice)

    def obtener_indice_jugador(self, jugador):
        contador = 0
        indice= 0
        for i in self.jugadores:
            if i.nombre == jugador.nombre:
                indice= contador
            contador +=1
        return indice


    def ronda(self, mazo, indice):
        for jugador in self.jugadores:
            carta = jugador.tomar_carta(mazo)
            if carta.es_1_de_oro():
                self.eliminar_jugador(indice)

    def finalizado(self):
        return len(self.jugadores) < 1

    def get_ganador(self):
        pass

    def eliminar_jugador(self, indice):
            del self.jugadores[indice]
