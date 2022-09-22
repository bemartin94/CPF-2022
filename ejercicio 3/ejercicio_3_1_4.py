import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "Punto en ({},{})".format(self.x, self.y)

    def cuadrante(self):
        if self.x >0 and self.y >0:
            return 1
        if self.x <0 and self.y >0:
            return 2
        if self.x <0 and self.y <0:
            return 3
        if self.x >0 and self.y <0:
            return 4
    
    def distancia_al_centro(self):
        return math.dist((self.x,self.y),(0,0))

    def __eq__(self, other):
        return self.x == other.punto_a and \
               self.y == other.y

    def get_x(self):
        return self.x

    def set_x(self, nuevo_valor):
        self.x =  nuevo_valor

    def get_y(self):
        return self.y

    def set_y(self,  nuevo_valor):
        self.y =  nuevo_valor
