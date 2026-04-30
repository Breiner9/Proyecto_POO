from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacerSonido(self):
        pass
        