class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def get_ruedas(self):
        return self.ruedas

    def get_color(self):
        return self.color

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        Vehiculo.__init__(self, color, ruedas)
        self.tipo =  tipo

    def get_tipo(self):
        return self.tipo

class VehiculoMotorizado(Vehiculo):
    def __init__(self, color, ruedas, combustible, distanciaRecorrida, relacionConsumoDistancia):
        Vehiculo.__init__(self, color, ruedas)
        self.combustible =  combustible
        self.distanciaRecorrida = distanciaRecorrida
        self.relacionConsumoDistancia = relacionConsumoDistancia

    def cargarCombustible(self, cantidad):
        self.combustible += cantidad

    def recorrerDistancia(self, distancia):
        if self.combustible >= self.relacionConsumoDistancia * distancia:
            self.distanciaRecorrida += distancia
            self.combustible -= self.relacionConsumoDistancia * distancia
        else:
            print("andá a la YPF")

class Coche(VehiculoMotorizado):
    def __init__(self, color, ruedas, combustible, distanciaRecorrida, relacionConsumoDistancia, velocidad, cilindrada):
        VehiculoMotorizado.__init__(self,color, ruedas, combustible, distanciaRecorrida, relacionConsumoDistancia)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def get_velocidad(self):
        return self.velocidad

    def get_cilindrada(self):
        return self.cilindrada


class Moto(Coche):
    def __init__(self, color, ruedas, combustible, distanciaRecorrida, relacionConsumoDistancia, velocidad, cilindrada, tipo):
        Coche.__init__(self, color, ruedas, combustible, distanciaRecorrida, relacionConsumoDistancia, velocidad, cilindrada)
        self.tipo = tipo

    def get_tipo(self):
        return self.tipo

class Camioneta(Coche):
    def __init__(self, color, ruedas, combustible, distanciaRecorrida, relacionConsumoDistancia, velocidad, cilindrada,carga):
        Coche.__init__(self, color, ruedas, combustible, distanciaRecorrida, relacionConsumoDistancia, velocidad, cilindrada)
        self.carga = carga

    def get_carga(self):
        return self.carga
