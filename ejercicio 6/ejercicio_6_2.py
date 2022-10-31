from abc import ABC, abstractmethod

class ObjetoDibujable(ABC):

    @abstractmethod
    def dibujar(self):
        pass


class Perro(ObjetoDibujable):
    def dibujar(self):
        print("\U0001F415")


class Figura(ObjetoDibujable):

    def __init__(self, nombre):
        self.nombre= nombre

    @abstractmethod
    def get_nombre(self):
        return self.nombre

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

    @abstractmethod
    def dibujar(self):
        pass

class Cuadrado(Figura):
    def __init__(self, medida, nombre, cantidad_de_lados=4):
        Figura.__init__(self, nombre)
        self.cantidad_de_lados= cantidad_de_lados
        self.medida= medida

    def calcular_area(self):
        return self.medida * self.medida

    def calcular_perimetro(self):
        return self.medida * self.cantidad_de_lados

    def dibujar(self):
        print("Soy un cuadrado de ", self.medida, "cm de lado")


class Rectangulo(Figura):
    def __init__(self, base, altura, nombre="rectangulo", cantidad_de_lados=4):
        Figura.__init__(self, nombre)
        self.cantidad_de_lados= cantidad_de_lados
        self.base= base
        self.altura=altura

    def get_nombre(self):
        return self.nombre

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return self.base + self.altura * 2

    def dibujar(self):
        print("Soy un resctangulo de ", self.base, "cm de lado y ", self.altura, " de altura")


perro = Perro()
perro.dibujar()
rect= Rectangulo(2,3)
print(rect.calcular_area())