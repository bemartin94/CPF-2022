#4.	Nos piden realizar una agenda telefónica de contactos.

#a.	Un contacto está definido por un nombre y un teléfono (No es necesario de validar).
# Un contacto es igual a otro cuando sus nombres son iguales.

#b.	Una agenda de contactos está formada por un conjunto de contactos (Piensa en que tipo puede ser)

#c.	Se podrá crear de dos formas, indicándoles nosotros el tamaño o con un tamaño por defecto (10)

# d.	Los métodos de la agenda serán los siguientes:
# i.	aniadirContacto(Contacto c): Añade un contacto a la agenda, sino se pueden meter más
#       a la agenda se indicara por pantalla. No se pueden meter contactos que existan, es decir, no podemos duplicar
#       nombres, aunque tengan distinto teléfono.
# ii.	existeContacto(Conctacto c): indica si el contacto pasado existe o no.
# iii.	listarContactos(): Lista toda la agenda
# iv.	buscaContacto(String nombre): busca un contacto por su nombre y muestra su teléfono.
# v.	eliminarContacto(Contacto c): elimina el contacto de la agenda, indica si se ha eliminado o no por pantalla
# vi.	agendaLlena(): indica si la agenda está llena.
# vii.	huecosLibres(): indica cuantos contactos más podemos meter.

#e.	Crea un menú con opciones por consola para probar todas estas funcionalidades.

#from claseContactoEj4 import Contacto
class Contacto:
    def __init__(self, nombre, apellido, telefono):
        self.nombre=nombre
        self.apellido=apellido
        self.telefono=telefono

class Agenda:
    def __init__(self):
        self.contactos = []
        self.LARGO_DE_AGENDA=11

    def añadir_contacto(self, nombre, telefono):
        contacto = Contacto(" "," ",0)
        contacto.nombre = nombre
        # contacto.apellido =
        contacto.telefono = telefono
        self.contactos.append(contacto)

    def existeContacto(self,nombre):
        for contacto in self.contactos: #---------------->lo saque del def imprimir
            if contacto.nombre == nombre:
                print("contacto existe")

    def buscaContacto(self,nombre): #------------------>tomar carta
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                print("contacto existe")
                print(contacto.telefono)

    def imprimir(self):
        for contacto in self.contactos:
            print(contacto.nombre, contacto.apellido, contacto.telefono)

    def eliminarContacto(self,nombre):
        contador=0
        for contacto in self.contactos:
            contador += 1
            if contacto.nombre == nombre:
                self.contactos.pop(contador) #------------>no hace la baja

    def agendaLlena(self):
        if len(self.contactos)<=self.LARGO_DE_AGENDA:
            return False#----------->con lugar
        else:
            return True  #----------->lleno

    def huecosLibres(self):
        libres=self.LARGO_DE_AGENDA-len(self.contactos)
        return libres






agenda =Agenda()

agenda.añadir_contacto(" ",0)
agenda.añadir_contacto("roberto", 12344321)
agenda.añadir_contacto("macoco", 43214321)
agenda.añadir_contacto("florentino", 1234123)
#agenda.añadir_contacto("robledo",98709870)
#agenda.existeContacto("macoco")
#agenda.buscaContacto("florentino")
agenda.imprimir()
#print(" ")
#agenda.eliminarContacto("florentino")
#print(" ")
#agenda.imprimir()
print((agenda.agendaLlena()))
print(agenda.huecosLibres())


print("1_INGRESE UN CONTACTO : ")
print("2_BUSCAR UN CONTACTO  : ")
print("3_BORRAR UN CONTACTO  : ")
print("4_ESPACIO DISPONIBLE  : ")
print("5_LISTAR LA AGENDA    : ")
print("6_SALIR DEL MENU")
numeroDeEleccion=int(input("ingrese su eleccion:"))



#___________________________________________________________________________________________________________


