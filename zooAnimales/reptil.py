from zooAnimales.animal import Animal
class Reptil(Animal):
    listado=[]
    iguanas=0
    serpientes=0
    total=0
    def __init__(self, nombre, edad, habitat, genero,color,large, zona=None):
        super().__init__(nombre, edad, habitat, genero, zona)
        self.colorEscamas=color
        self.largoCola=large
        self.listado.append(self)
        
    @classmethod
    def crearSerpiente(cls,name,int,genero):
        nuevo=Reptil(name,int,"humedal",genero,"verde",3)
        cls.serpientes+=1
        return nuevo
    @classmethod
    def crearIguana(cls,name,edad,genero):
        nuevo=Reptil(name,edad,"humedal",genero,"verde",3)
        cls.iguanas+=1
        return nuevo
    @classmethod 
    def cantidadReptiles(cls):
        contador=cls.iguanas+cls.serpientes+cls.total
        return contador
    def movimiento():
        return "reptar"
    def getColorEscamas(self):
        return self.colorEscamas

    def setColorEscamas(self, colorEscamas):
        self.colorEscamas = colorEscamas

    def getLargoCola(self):
        return self.largoCola

    def setLargoCola(self, largoCola):
        self.largoCola = largoCola
