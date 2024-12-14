from zooAnimales.animal import Animal
class Ave(Animal):
    listado=[]
    halcones=0
    aguilas=0
    total=0
    def __init__(self, nombre, edad, habitat, genero, piernas ,zona=None):
        super().__init__(nombre, edad, habitat, genero, zona)
        self.colorPlumas=piernas
        Ave.listado.append(self)
        Ave.total=+1
    def movimiento(self):
        return "volar"
    @classmethod
    def cantidadAves(cls):
        contador=cls.aguilas+cls.halcones+cls.total
        return contador
    @classmethod
    def crearHalcon(cls,name,edad,genero):
        nuevom=Ave(name,edad,"montanas",genero,"cafe glorioso") 
        cls.halcones+=1
        return nuevom
    @classmethod
    def crearAguila(cls,name,edad,genero):
        nuevom=Ave(name,edad,"montanas",genero,"blanco y amarillo")   
        cls.aguilas+=1
        return nuevom
    def getColorPlumas(self):
        return self.colorPlumas

    def setColorPlumas(self, colorPlumas):
        self.colorPlumas = colorPlumas
   