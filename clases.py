class Personas: # CLASE PADRE
    atributo = 123

    def __init__(self, nombre, edad): # Constructor
        self.nombre = nombre
        self.edad = edad

    def birthday(self): # Funcion de uso exclusivo por la clase Personas. Self como tal no es un parametro.
        self.edad += 1
        print(f"Feliz cumpleanios #{self.edad} {self.nombre}")

class Empleado(Personas):
    def __init__(self, horasTotales, nombre, edad): 
        super(Empleado, self).__init__(nombre, edad)
        self.horasTotales = horasTotales

    def trabajador(self, horasTrabajadas):
        print(f"Usted ha trabajado {horasTrabajadas} horas")
        print(f"Horas totales trabajadas {self.horasTotales}")

pedro = Personas(nombre="Pedro",edad= 20)
print(pedro.edad)
print(pedro.nombre)
print(pedro.atributo)


pedro.birthday()

paco = Empleado(nombre= "Paco", edad= 25, horasTotales= 25)
paco.trabajador(8)
paco.birthday()