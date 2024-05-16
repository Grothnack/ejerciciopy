class Persona:
    def __init__(self, nombre='', edad=0, DNI='', telefono='', email=''):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI
        self.telefono = telefono
        self.email = email

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setEdad(self, edad):
        self.edad = edad

    def getEdad(self):
        return self.edad

    def setDNI(self, DNI):
        self.DNI = DNI

    def getDNI(self):
        return self.DNI

    def setTelefono(self, telefono):
        self.telefono = telefono

    def getTelefono(self):
        return self.telefono

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

    def mostrar(self):
        print(f'Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.DNI}, Teléfono: {self.telefono}, Email: {self.email}')

    def esMayorDeEdad(self):
        return self.edad >= 18
