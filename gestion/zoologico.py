class Zoologico:
    def __init__(self, nombre, ubicacion):
        self.nombre=nombre
        self.ubicaion=ubicacion
        self.zona=[]
    def agregarZonas(self,lugar):
        self.zona.append(lugar)
        lugar.setZoo(self)
    def cantidadTotalAnimales(self):
        contador=0
        for i in range(len(self.zona)):
            contador=self.zona[i].cantidadAnimales()+contador
        return contador
    def setNombre(self, nuevo):
        self.nombre = nuevo

    def getNombre(self):
        return self.nombre

    def setUbicacion(self, ubi):
        self.ubicacion = ubi

    def getUbicacion(self):
        return self.ubicacion

    def setZona(self, zonas):
        self.zona = zonas

    def getZona(self):
        return self.zona

        
