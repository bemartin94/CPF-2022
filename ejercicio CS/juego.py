from jugador import Jugador
from mazo import Mazo

class Juego:
    def __init__(self, jugadores, mazo):
        self.jugadores = jugadores
        self.mazo = mazo

    def iniciar(self):
        self.mazo.mezclar()
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
            contador +=1
            if carta.es_1_de_oro():
               indice = self.obtener_indice_jugador(self.jugadores)
               self.eliminar_jugador(indice)
               salio_el_1_de_oro = True
            if contador == 2:
                contador = 0

    def finalizado(self):
        return len(self.jugadores) < 1

    def get_ganador(self):
        if self.finalizado():
            return self.jugadores

    def eliminar_jugador(self, indice):
         del self.jugadores[indice]

jugadores = [Jugador("Ignacio"), Jugador("Asbel"), Jugador("Angel")]
mazo = Mazo()
juego = Juego(jugadores=jugadores, mazo=mazo)
juego.iniciar()
print(juego.get_ganador())
#en eliminar jugador paso como parametro el metodo obtener_indice
