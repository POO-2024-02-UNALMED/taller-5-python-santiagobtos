class Zona():
    def __init__(self,nombre,zoo):
        self.nombre=nombre
        self.zoo=zoo
        self.animales=[]
    def cantidadAnimales(self):
        return len(self._animales)
    def agregarAnimales(self,animal):
        self._animales.append(animal)
    def setNombre(self, nuevo):
        self.nombre = nuevo

    def getNombre(self):
        return self.nombre

    def setZoo(self, zo):
        self.zoo = zo

    def getZoo(self):
        return self.zoo
