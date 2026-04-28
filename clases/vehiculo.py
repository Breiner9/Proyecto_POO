class Vehiculo:
    #Usamos un constructor para definir nuestros atributos
    def __init__(self):
        self.velocidad = 0
         
    #Creamos un método      
    def acelerar(self):
        self.velocidad += 10
        
        