class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return "{},{}".format(self.nombre, self.telefono)


class Agenda:
    def __init__(self, cantidad_de_contactos =10):
        self.contactos = []
        self.cantidad_de_contactos = cantidad_de_contactos

    def anadirContacto(self, contacto):
        pass

    def existeContacto(self, contacto):
        pass

    def listarContactos(self):
        pass

    def buscaContacto(self, stringNombre):
        pass

    def eliminarContacto(self, contacto):
        pass

    def agendaLlena(self):
        pass

    def huecosLibres(self):
        pass
