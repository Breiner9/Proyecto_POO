#Importamos nuestra clase animal
from clases.animal import Animal

#Nuestra clase perro hereda Animal
class Perro(Animal):
    
#Implementamos nuestro metodo para perro   
    def hacerSonido(self):
        print("Sonido Perro: Sniff-sniff-snifffff")