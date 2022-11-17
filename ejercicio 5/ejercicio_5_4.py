class Empleado:
    PLUS = 300
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario= salario

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def get_salario(self):
        return self.salario

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def set_edad(self, nueva_edad):
        self.edad = nueva_edad

    def set_salario(self, nuevo_salario):
        self.salario = nuevo_salario

    def __str__(self):
        return "EL nombre del empleado es {}".format(self.nombre)

    def plus(self):
        pass

class Comercial(Empleado):
    def __init__(self, nombre, edad, salario, comision):
        Empleado.__init__(self, nombre, edad, salario)
        self.comision = comision

    def plus(self):
        if self.edad > 30 and self.comision > 200:
            self.salario += self.PLUS



class Repartidor(Empleado):
    def __init__(self, nombre, edad, salario, zona):
        Empleado.__init__(self, nombre, edad, salario)
        self.zona = zona

    def plus(self):
        if self.edad < 25 and self.zona == "zona 3":
            self.salario += self.PLUS

uno= Comercial("jose", 50, 4000, 2000)
uno.plus()
print(uno.salario)


