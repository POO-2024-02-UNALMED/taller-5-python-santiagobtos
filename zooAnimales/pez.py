from zooAnimales.animal import Animal
class Pez(Animal):
    listado=[]
    salmones=0
    bacalaos=0
    total=0
    def __init__(self, nombre, edad, habitat, genero,color,caletas ,zona=None):
        super().__init__(nombre, edad, habitat, genero, zona)
        self.colorEscamas=color
        self.cantidadAletas=caletas
        Pez.listado.append(self)
        Pez.total+=1
    @classmethod
    def crearBacalao(cls,name,edad,genero):
        nuevo=Pez(name,edad,"oceano",genero,"gris",6)
        cls.bacalaos+=1
        return nuevo
    @classmethod
    def crearSalmon(cls,name,edad,genero):
        nuevo=Pez(name,edad,"oceano",genero,"rojo",6)
        cls.bacalaos+=1
        return nuevo
    @classmethod
    def cantidadPeces(cls):
        contador=cls.salmones+cls.bacalaos+cls.total
        return contador
    def movimiento():
        return "nadar"
    def getColorEscamas(self):
        return self.colorEscamas

    def setColorEscamas(self, colorEscamas):
        self.colorEscamas = colorEscamas

    def getCantidadAletas(self):
        return self.cantidadAletas

    def setCantidadAletas(self, cantidadAletas):
        self.cantidadAletas = cantidadAletas