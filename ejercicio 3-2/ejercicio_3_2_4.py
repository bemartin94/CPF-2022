class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return "{},{}".format(self.nombre, self.telefono)

class Agenda:
    def __init__(self, cantidad_de_contactos = 10):
        self.contactos = []
        self.cantidad_de_contactos = cantidad_de_contactos

    def anadirContacto(self, nombre, telefono):
        contacto = Contacto("","")
        if not self.agendaLlena():
            if not self.existeContacto(nombre):
                contacto.nombre = nombre
                contacto.telefono = telefono
                self.contactos.append(contacto)
                print("Contacto agregado", contacto)

        else:
            print("No se pudo agregar el contacto")

    def existeContacto(self, stringNombre):
        for contacto in self.contactos:
            if contacto.nombre == stringNombre:
                return True

    def listarContactos(self):
        for contacto in self.contactos:
            print(contacto.__str__())

    def buscaContacto(self, stringNombre):
        for contacto in self.contactos:
                if contacto.nombre == stringNombre:
                    return contacto.telefono
                else:
                    print("No se encontró un contacto con ese nombre")

    def eliminarContacto(self, contacto):
        self.contactos.nombre.remove(contacto)
        print("Se eliminó el contacto especificado")

    def agendaLlena(self):
        return len(self.contactos) == self.cantidad_de_contactos - 1

    def huecosLibres(self):
        return self.cantidad_de_contactos - len(self.contactos)

nueva_agenda = Agenda()
opcion= None
while not opcion== 0:
    print("Agenda virtual")
    print("1- CREAR CONTACTO")
    print("2- VER TODOS LOS CONTACTOS")
    print("3- BUSCAR CONTACTO")
    print("4- ELIMINAR CONTACTO")
    print("5- VER ESPACIO DISPONIBLE")
    print("0- SALIR")
    opcion = int(input("Ingrese el número de la opción a seleccionar"))
    if opcion ==1:
        nombre = input("Ingrese el nombre del contacto")
        numero = input("Ingrese el numero del contacto")
        nueva_agenda.anadirContacto(nombre, numero)
    elif opcion ==2:
        print(nueva_agenda.listarContactos())
    elif opcion ==3:
        nombre = input("Ingrese el nombre del contacto a buscar")
        print(nueva_agenda.buscaContacto(nombre))
    elif opcion ==4:
        nombre = input("Ingrese el nombre del contacto a eliminar")
        print(nueva_agenda.eliminarContacto(nombre))
    elif opcion == 5:
        print("Te quedan", nueva_agenda.huecosLibres(), "espacios libres")

