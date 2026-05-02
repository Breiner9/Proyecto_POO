#Importamos nuestra clase vehiculo para que coche la pueda heredar
from clases.vehiculo import Vehiculo
from clases.excepciones import ExcesoVelocidadException

#Creamos la clase coche heredando atributos de vehiculo
class Coche(Vehiculo):
        def __init__(self,marca,modelo,anio, motor):
            super().__init__()
            self.__marca = marca
            self.__modelo = modelo 
            self.__anio = anio 
            self.motor = motor 

#====================================================================
# GETTERS Y SETTERS
#====================================================================

#Me muestra el dato que quiero
        def getmarca(self):
            return self.__marca

        def getmodelo(self):
            return self.__modelo
       
        def getanio(self):
            return self.__anio

#Puedo cambiar el dato que quiera
        def setmarca(self,marca):
            self.__marca = marca

        def setmodelo(self,modelo):
            self.__modelo = modelo

        def setanio(self, anio):
            self.__anio =  anio 

#====================================================================
# METODOS PROPIOS 
#====================================================================     

#Creamos el metodo describir para coche
        def describir(self):
            print(f"Marca: {self.__marca}")
            print(f"Modelo: {self.__modelo}")
            print(f"Anio: {self.__anio}")
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
            