import random

class Revolver:
    def __init__(self, posicion_actual =0, posicion_bala=3, tambor=["o","o","o","o","o","o"]):
        self.posicion_actual = posicion_actual
        self.posicion_bala = posicion_bala
        self.tambor = tambor


    def disparar(self):
        return self.posicion_actual == self.posicion_bala

    def siguiente_bala(self):
        self.posicion_actual += 1

    def girar_tambor(self):
        self.posicion_actual = random.randint(0, len(self.tambor))

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

    def disparar(self, revolver):
        if revolver.disparar() == True:
            self.esta_vivo == False

class Juego:
    pass

rev = Revolver()
print(rev)
rev.imprimir_revolver()