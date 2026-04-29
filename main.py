from clases.vehiculo import Vehiculo
from clases.motor import Motor
from clases.coche import Coche
from clases.bicicleta import Bicicleta
#NOTA: no imprimimos acelerar en coche ni en bici porque lo hacemos en la lista para que no se duplique la velocidad
#Creamos un objeto para vehiculo
vehiculo1 = Vehiculo()

print(f"Velocidad Inicial: {vehiculo1.velocidad}")
vehiculo1.acelerar()
print(f"Velocidad Actual: {vehiculo1.velocidad}\n")
 

#Creamos un objeto para motor
motor1 = Motor("283 CV","Electrico")

#Creamos un objeto para coche 

coche1 = Coche("Tesla", "Model 3", 2024, motor1)

coche1.describir()
print(f"Velocidad: {coche1.velocidad}km/h\n")

#Creamos un objeto para bicicleta
bicicleta1 = Bicicleta("Montaña",6)

bicicleta1.describir()
print(f"Velocidad: {bicicleta1.velocidad}km/h\n")

#Creamos una lista para ver el comportamiento de nuestros objetos
transportes =([coche1,bicicleta1])

for transporte in transportes:
    transporte.describir()
    transporte.acelerar()
    print(f"Velocidad: {transporte.velocidad} km/h\n")

