class Instrumento:
    def __init__(self, precio, marca, modelo):
        self.precio = precio
        self.marca = marca
        self.modelo = modelo

    def tocar(self):
        pass

class Guitarra(Instrumento):
    def tocar(self):
        print("Sonando como una guitarra")

class Bateria(Instrumento):
    def tocar(self):
        print("Sonando como una bateria")

class Piano(Instrumento):
    def tocar(self):
        print("Sonando como un piano")



