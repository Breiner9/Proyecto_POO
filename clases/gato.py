#Importamos clase animal 
from clases.animal import Animal

#Clase gato que hereda animal
class Gato(Animal):

#Implementamos el metodo con su respectivo sonido
    def hacerSonido(self):
        print("Sonido Gato: Miaaauu-Miaaauu...")
