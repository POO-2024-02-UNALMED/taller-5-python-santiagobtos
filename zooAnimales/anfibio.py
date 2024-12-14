from zooAnimales.animal import Animal
class Anfibio(Animal):
    listado=[]
    ranas=0
    salamandras=0
    total=0
    def __init__(self, nombre, edad, habitat, genero,color,venenoso, zona=None):
        super().__init__(nombre, edad, habitat, genero, zona)
        self.colorPiel=color
        self.venenoso=venenoso
        Anfibio.listado.append(self)
        Anfibio.total+=1

    @classmethod
    def crearRana(cls,name,edad,genero):
        nuevo=Anfibio(name,edad,"selva",genero,"rojo",True)
        cls.ranas+=1
        return nuevo
    @classmethod
    def crearSalamandra(cls,name,edad,genero):
        nuevo=Anfibio(name,edad,"selva",genero,"negro y amarillo",False)
        cls.salamandras+=1
        return nuevo
    @classmethod
    def cantidadAnfibios(cls):
        contador=cls.salamandras+cls.ranas+cls.total
        return contador
    def movimiento():
        return "saltar"
    def getColorPiel(self):
        return self.colorPiel

    def setColorPiel(self, colorPiel):
        self.colorPiel = colorPiel

    def isVenenoso(self):
        return self.venenoso

    def setVenenoso(self, venenoso):
        self.venenoso = venenoso