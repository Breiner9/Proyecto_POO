#Importamos nuestra clase vehiculo para que coche la pueda heredar
from clases.vehiculo import Vehiculo
from clases.excepciones import ExcesoVelocidadException
#Creamos la clase coche heredando atributos de vehiculo
class Coche(Vehiculo):
        def __init__(self,marca,modelo,anio, motor):
            super().__init__()
            self.marca = marca
            self.modelo = modelo 
            self.anio = anio 
            self.motor = motor 

#Creamos el método describir       
        def describir(self):
            print(f"Marca: {self.marca}")
            print(f"Modelo: {self.modelo}")
            print(f"Anio: {self.anio}")
            print(f"Potencia Motor: {self.motor.potencia}")
            print(f"Tipo Motor: {self.motor.tipo}")

#Creamos el método acelerar para coche
        def acelerar(self):
            self.velocidad += 200

#Creamos el metodo incrementar velocidad para coche 
        def incrVelocidad(self, velocidad):
            self.velocidad += velocidad
            if self.velocidad > 200:
                raise ExcesoVelocidadException("¡¡¡ATENCION!! EXCESO DE VELOCIDAD")
            