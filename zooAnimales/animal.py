from gestion.zona import zona
class Animal():
    totalAnimales=None
    def __init__(self,nombre,edad,habitat,genero,zona=None):
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
        self._zona=zona
        Animal.totalAnimales+=1
    def totalPorTipo():
        return "Mamíferos: " + str(Mamifero.cantidad_mamiferos()) + "\n" + \
            "Aves: " + str(Ave.cantidad_aves()) + "\n" + \
            "Reptiles: " + str(Reptil.cantidad_reptiles()) + "\n" + \
            "Peces: " + str(Pez.cantidad_peces()) + "\n" + \
            "Anfibios: " + str(Anfibio.cantidad_anfibios())
    def __str__(self):
        if self._zona!=None:
            return "Mi nombre es " + self._nombre + ", tengo una edad de " +self._edad + ", habito en " + self._habitat+ " y mi genero es " + self._genero + ", la zona en la que me ubico es " + self._zona.getNombre() + " y mi genero es " + self._genero
        else:
            return "Mi nombre es " + self._nombre + ", tengo una edad de " + self._edad + ", habito en " + self._habitat + " y mi genero es " + self._genero
    def movimiento():
        return "desplazarse"
    def getTotalAnimales(self):
        return self.totalAnimales

    def setTotalAnimales(self, totalAnimales):
        self.totalAnimales = totalAnimales

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getEdad(self):
        return self.edad

    def setEdad(self, edad):
        self.edad = edad

    def getHabitat(self):
        return self.habitat

    def setHabitat(self, habitat):
        self.habitat = habitat

    def getGenero(self):
        return self.genero

    def setGenero(self, genero):
        self.genero = genero

    def getZona(self):
        return self.zona

    def setZona(self, zona):
        self.zona = zona

