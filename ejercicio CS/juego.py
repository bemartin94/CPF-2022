from jugador import Jugador
from mazo import Mazo

class Juego:
    def __init__(self, jugadores, mazo):
        self.jugadores = jugadores
        self.mazo = mazo

    def iniciar(self):
        while not self.finalizado():
            self.juego()

    def obtener_indice_jugador(self, jugador):
        contador = 0
        indice= 0
        for i in self.jugadores:
            if i.nombre == jugador.nombre:
                indice= contador
            contador +=1
        return indice

    def juego(self):
        salio_el_1_de_oro = False
        contador = 0
        while not salio_el_1_de_oro:
            carta = self.jugadores[contador].tomar_carta(self.mazo)
            if carta.es_1_de_oro():
               indice = contador
               self.eliminar_jugador(indice)
               self.mazo.cartas = self.mazo.generar_mazo()
               salio_el_1_de_oro = True
            if contador == (len(self.jugadores) - 1):
                contador = -1
            contador +=1

    def finalizado(self):
        return len(self.jugadores) <= 1

    def get_ganador(self):
        if self.finalizado():
            return self.jugadores

    def imprimir_ganador(self):
        jugadores = self.get_ganador()
        jugador_ganador = jugadores[0]
        print("El ganador es {}".format(jugador_ganador.nombre))

    def eliminar_jugador(self, indice):
         del self.jugadores[indice]

jugadores = [Jugador("Ignacio"), Jugador("Asbel"), Jugador("Angel")]
mazo = Mazo()
#print(mazo.imprimir_mazo())

juego = Juego(jugadores=jugadores, mazo=mazo)
juego.iniciar()
juego.imprimir_ganador()
#en eliminar jugador paso como parametro el metodo obtener_indice
