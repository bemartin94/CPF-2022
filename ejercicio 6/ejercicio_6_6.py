from abc import ABC, abstractmethod

class Puerta(ABC):
    pass

class PuertaBloqueable(Puerta):
    pass

class Alarma(ABC):
    pass
    def activarAlarma(self):
        pass

    def desactivarAlarma(self):
        pass

class ComponenteDeCoche:
    def __init__(self,descripcion, peso, coste):
        self.descripion = descripcion
        self.peso= peso
        self.coste = coste

class PuertaCoche(ComponenteDeCoche):
    def __init__(self, descripcion, peso, coste):
        ComponenteDeCoche.__init__(self, descripcion, peso, coste)
        self.estaBloqueada= True