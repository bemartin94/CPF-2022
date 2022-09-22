import math

class Segmento:
    def __init__(self, punto_a, punto_b):
        self.punto_a = punto_a
        self.punto_b = punto_b

    def __str__(self):
        return "Punto A: {} - Punto B: {}".format(self.punto_a, self.punto_b)

    def get_punto_a(self):
        return self.punto_a

    def set_punto_a(self, nuevo_valor):
        self.punto_a =  nuevo_valor

    def get_punto_b(self):
        return self.punto_b

    def set_punto_b(self,  nuevo_valor):
        self.punto_b =  nuevo_valor

    def longitud_segmento(self):
        return math.dist((self.punto_a.x,self.punto_a.y),(self.punto_b.x,self.punto_b.y))
