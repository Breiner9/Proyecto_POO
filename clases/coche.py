#Importamos nuestra clase vehiculo para que coche la pueda heredar
from clases.vehiculo import Vehiculo

#Creamos la clase coche heredando atributos de vehiculo
class Coche(Vehiculo):
        def __init__(self,marca,modelo,anio):
            super().__init__()
            self.marca = marca
            self.modelo = modelo 
            self.anio = anio 
            
#Creamos el método describir       
        def describir(self):
            print(f"Marca: {self.marca}")
            print(f"Modelo: {self.modelo}")
            print(f"Anio: {self.anio}")

#Creamos el método acelerar para coche
        def acelerar(self):
            self.velocidad += 200
            