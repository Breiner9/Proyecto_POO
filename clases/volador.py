#Clase abstracta Volador
#Representa objetos que pueden volar
from abc import ABC, abstractmethod

class Volador(ABC):

#Metodo que deben implementar las clases hijas 
    @abstractmethod
    def volar(self):
        pass