#Importamos la clase vehiculo ya que bicicleta va a heredarla
from clases.vehiculo import Vehiculo

#Creamos la clase bicicleta heredando atributos de vehiculo
class Bicicleta(Vehiculo):
    def __init__(self, tipo,num_velocidades):
        super().__init__()
        self.num_velocidades = num_velocidades
        self.tipo = tipo 
#Creamos el método
    def describir(self):
        print(f"Velocidades: {self.num_velocidades}")
        print(f"Tipo: {self.tipo}")       
#Creamos le método acelerar 
    def acelerar(self):
        self.velocidad += 10
