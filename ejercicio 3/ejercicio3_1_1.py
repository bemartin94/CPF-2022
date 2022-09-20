class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_perimetro(self):
        return 2*self.base + 2*self.altura

    def calcular_area(self):
        return self.base*self.altura

    def get_base(self):
        return self.nombre

    def set_base(self, nueva_base):
        self.base = nueva_base

    def get_altura(self):
        return self.altura

    def set_altura(self, nueva_altura):
        self.altura = nueva_altura