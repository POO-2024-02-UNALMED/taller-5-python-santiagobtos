from anfibio import Anfibio
from ave import Ave
from reptil import Reptil
from pez import Pez
from mamifero import Mamifero


class Animal():
    totalAnimales=0
    def __init__(self,nombre,edad,habitat,genero,zona=None):
        self.nombre=nombre
        self.edad=edad
        self.habitat=habitat
        self.genero=genero
        self.zona=zona
        Animal.totalAnimales+=1
    def totalPorTipo():
        return "Mamíferos: " + str(Mamifero.cantidadMamiferos()) + "\n" + \
            "Aves: " + str(Ave.cantidadAves()) + "\n" + \
            "Reptiles: " + str(Reptil.cantidadReptiles()) + "\n" + \
            "Peces: " + str(Pez.cantidadPeces()) + "\n" + \
            "Anfibios: " + str(Anfibio.cantidadAnfibios())
    def toString(self):
        if self._zona!=None:
            return "Mi nombre es " + self.nombre + ", tengo una edad de " +self.edad + ", habito en " + self.habitat+ " y mi genero es " + self._genero + ", la zona en la que me ubico es " + self._zona.getNombre() + " y mi genero es " + self._genero
        else:
            return "Mi nombre es " + self.nombre + ", tengo una edad de " + self.edad + ", habito en " + self.habitat + " y mi genero es " + self._genero
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

