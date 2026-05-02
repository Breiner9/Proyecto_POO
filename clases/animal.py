#Clase abstracta
#Define el comportamiento comun: hacer sonido 
from abc import ABC, abstractmethod

class Animal(ABC):
    
#Metodo que deben implementar las clases hijas     
    @abstractmethod
    def hacerSonido(self):
        pass
        