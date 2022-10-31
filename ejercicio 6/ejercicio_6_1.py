from abc import ABC, abstractmethod

class Roedores(ABC):
    @abstractmethod
    def comer(self):
        pass

    @abstractmethod
    def correr(self):
        pass

    @abstractmethod
    def olfatear(self):
        pass

    @abstractmethod
    def trepar(self):
        pass

class Gerbo(Roedores):
    def comer(self):
        print("Estoy comiendo como un Gerbo")

    def correr(self):
        print("Estoy corriendo como un Gerbo")

    def olfatear(self):
        print("Estoy olfateando como un Gerbo")

    def trepar(self):
        print("Estoy trepando como un Gerbo")

class Hamster(Roedores):
    def comer(self):
        print("Estoy comiendo como un Hámster")

    def correr(self):
        print("Estoy corriendo como un Hámster")

    def olfatear(self):
        print("Estoy olfateando como un Hámster")

    def trepar(self):
        print("Estoy trepando como un Hámster")

class Raton(Roedores):
    def comer(self):
        print("Estoy comiendo como un Raton")

    def correr(self):
        print("Estoy corriendo como un Raton")

    def olfatear(self):
        print("Estoy olfateando como un Raton")

    def trepar(self):
        print("Estoy trepando como un Raton")

class HamsterAzul(Hamster):
    pass
