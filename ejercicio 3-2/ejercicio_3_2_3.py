import random

class Revolver:
    def __init__(self, posicion_actual =0, posicion_bala=3, tambor=["o","o","o","o","o","o"]):
        self.posicion_actual = posicion_actual
        self.posicion_bala = posicion_bala
        self.tambor = tambor


    def coincide_posicion(self):
        return self.posicion_actual == self.posicion_bala

    def siguiente_bala(self):
        self.posicion_actual += 1

    def girar_tambor(self):
        self.posicion_actual = random.randint(0, len(self.tambor))
        return self.posicion_actual

    def imprimir_revolver(self):
        revolver= self.posicion_actual
        print(" {}".format(revolver))

    def get_posicion(self):
        return self.posicion_actual

class Jugador:
    def __init__(self, id, nombre, esta_vivo = True):
        self.id= id
        self.nombre = nombre
        self.esta_vivo = esta_vivo

    def get_estavivo(self):
        return self.esta_vivo

    def disparar(self, revolver):
        if revolver.coincide_posicion() == True:
            self.esta_vivo = False

class Juego:
    def __init__(self, jugadores,revolver):
        self.jugadores = jugadores
        self.revolver = revolver

    def termino_el_juego(self):
        return len(self.jugadores) <= 1

    def eliminar_jugador(self, indice):
         del self.jugadores[indice]

    def jugar(self, revolver):
        contador = 0
        while not self.termino_el_juego():
            self.revolver.girar_tambor()
            if self.revolver.coincide_posicion():
                indice = contador
                self.jugadores[indice].disparar(revolver)
                self.eliminar_jugador(indice)
            if contador == (len(self.jugadores) - 1):
                contador = -1
            contador += 1

    def get_ganador(self):
        if self.termino_el_juego():
            return self.jugadores

    def imprimir_ganador(self):
        jugadores = self.get_ganador()
        jugador_ganador = jugadores[0]
        print("El ganador es {}".format(jugador_ganador.nombre))


rev = Revolver()
print(rev)
rev.imprimir_revolver()
print(rev.girar_tambor())
jugadores = [Jugador(0, "Ignacio"), Jugador(1, "Asbel"), Jugador(2, "Angel")]
juego = Juego(jugadores, rev)
juego.jugar(rev)
juego.imprimir_ganador()
print(jugadores[0].get_estavivo())