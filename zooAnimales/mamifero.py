from zooAnimales.animal import Animal
class Mamifero(Animal):
    caballos=0
    leones=0
    total=0
    listado=[]
    def __init__(self, nombre, edad, habitat, genero, estao, leg , zona=None):
        super().__init__(nombre, edad, habitat, genero, zona)
        self.patas=leg
        self.pelaje=estao
        Mamifero.listado.append(self)
        
    @classmethod
    def crearCaballo(cls, nombre , edad , generito):
        nuevom=Mamifero(nombre,edad,"pradera",generito,True,4)
        cls.caballos+=1
        return nuevom
    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        nuevom=Mamifero(nombre,edad,"selva",genero,True,4)
        cls.leones+=1
        return nuevom
    @classmethod
    def cantidadMamiferos(cls):
        contador=cls.caballos+cls.leones+cls.total
        return contador
    def isPelaje(self):
        return self.pelaje

    def setPelaje(self, pelaje):
        self.pelaje = pelaje

    def getPatas(self):
        return self.patas

    def setPatas(self, patas):
        self.patas = patas

