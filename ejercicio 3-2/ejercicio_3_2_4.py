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
        if len(self.contactos) <= self.cantidad_de_contactos - 1:
            self.contactos.append(contacto)
            print("Contacto agregado")
        else:
            print("Agenda completa")

    def existeContacto(self, contacto):
        return contacto in self.contactos

    def listarContactos(self):
        return self.contactos

    def buscaContacto(self, stringNombre):
        for contacto in self.contactos:
                if contacto.nombre == stringNombre:
                    return contacto.telefono
                else:
                    print("No se encontró un contacto con ese nombre")

    def eliminarContacto(self, contacto):
        self.contactos.remove(contacto)
        print("Se eliminó el contacto especificado")

    def agendaLlena(self):
        pass

    def huecosLibres(self):
        pass
