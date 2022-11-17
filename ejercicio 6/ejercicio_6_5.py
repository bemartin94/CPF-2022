from abc import ABC, abstractmethod

class Direccion:
    def __init__(self, calle, ciudad, cp, pais):
        self.calle = calle
        self.ciudad =ciudad
        self.cp = cp
        self.pais= pais

class Humano(ABC):

    def identificate(self):
        return type

class Persona(Humano):
    def __init__(self, nombre, apellido, dni, direccion):
        self.nombre =nombre
        self.apellido = apellido
        self.dni= dni
        self.direccion = direccion

class Estudiante(Persona):
    def __init__(self, id, nombre, apellido, dni, direccion):
        Persona.__init__(self, nombre, apellido, dni, direccion)
        self.id = id

class Profesor(Persona):
    def __init__(self, despacho, nombre, apellido, dni, direccion):
        Persona.__init__(self, nombre, apellido, dni, direccion)
        self.despacho = despacho


est= Estudiante(1, "raul", "portal", "2345", Direccion("cabello", "caba", 1425, "argentina"))
print(est.identificate())