from clases.vehiculo import Vehiculo
from clases.motor import Motor
from clases.coche import Coche
from clases.bicicleta import Bicicleta
from clases.excepciones import ExcesoVelocidadException
#NOTA: no imprimimos acelerar en coche ni en bici porque lo hacemos en la lista para que no se duplique la velocidad


#Creamos un objeto para vehiculo 
print("=== Bloque 1: Vehiculo ===")
vehiculo1 = Vehiculo()
print(f"Velocidad inicial: {vehiculo1.velocidad} km/h")
vehiculo1.acelerar()
print(f"Velocidad actual: {vehiculo1.velocidad} km/h")
print()

#Creamos un objeto para coche 
print("=== Bloque 2: Coche con motor ===")
motor1 = Motor("283 CV", "Electrico")
coche1 = Coche("Tesla", "Model 3", 2024, motor1)
coche1.describir()
coche1.acelerar()
print(f"Velocidad: {coche1.velocidad} km/h")
print()

#Creamos un objeto para bicicleta
print("=== Bloque 3: Bicicleta ===")
bicicleta1 = Bicicleta("Montaña", 6)
bicicleta1.describir()
bicicleta1.acelerar()
print(f"Velocidad: {bicicleta1.velocidad} km/h")
print()

#Para no repetir las impresiones hechas, creamos otros objetos para darle orden 
print("=== Bloque 4: Polimorfismo ===")
motor2 = Motor("150 CV", "Gasolina")
coche2 = Coche("Mazda", "3", 2022, motor2)
bicicleta2 = Bicicleta("Ruta", 8)

transportes = [coche2, bicicleta2]

for transporte in transportes:
    transporte.describir()
    transporte.acelerar()
    print(f"Velocidad: {transporte.velocidad} km/h")

#Creamos una excepcion para coche 
print("====== Bloque 5: Excepciones ========")

motor3 = Motor("120 CV", "Gasolina")
coche3 = Coche("Ford", "Focus", 2020, motor3)

try:
    coche1.incrVelocidad(250)
except ExcesoVelocidadException as e:
    print(e)
