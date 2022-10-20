class VehiculoMotorizado:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def get_ruedas(self):
        return self.ruedas

    def get_color(self):
        return self.color
    
class Coche(VehiculoMotorizado):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        VehiculoMotorizado.__init__(self,color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def get_velocidad(self):
        return self.velocidad

    def get_cilindrada(self):
        return self.cilindrada


class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        Coche.__init__(self, color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def get_carga(self):
