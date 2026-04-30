from clases.vehiculo import Vehiculo
from clases.motor import Motor
from clases.coche import Coche
from clases.bicicleta import Bicicleta
from clases.excepciones import ExcesoVelocidadException
from clases.animal import Animal
from clases.gato import Gato
from clases.perro import Perro

# Prueba la creación de varios objetos Coche y su método describir.
def ejercicio_1():
    print("=== Ejercicio 1: Clase basica ===")

    motor1 = Motor("283 CV", "Electrico")
    motor2 = Motor("150 CV", "Gasolina")
    motor3 = Motor("200 CV", "Hibrido")

    coche1 = Coche("Tesla", "Model 3", 2024, motor1)
    coche2 = Coche("Mazda", "3", 2022, motor2)
    coche3 = Coche("Toyota", "Corolla", 2023, motor3)

    coche1.describir()
    print()

    coche2.describir()
    print()

    coche3.describir()
    print()

#Prueba para traer y cambiar datos con get y set 

def ejercicio_2():
    print("=== Ejercicio 2: Encapsulamiento ===")

    motor1 = Motor("283 CV", "Electrico")
    coche1 = Coche("Tesla", "Model 3", 2024, motor1)

    print("Datos iniciales del coche 1 ")
    coche1.describir()

    print("--- Modificando datos con setters ---")
    coche1.setmarca("Volkswagen")
    coche1.setmodelo("Gol")
    coche1.setanio(2020)

    print(f"Marca modificada: {coche1.getmarca()}")
    print(f"Modelo modificado: {coche1.getmodelo()}")
    print(f"Anio modificado: {coche1.getanio()}")

    print("--- Coche 1 despues de setters ---")
    coche1.describir()

# Prueba que el constructor inicializa correctamente los atributos del coche.
def ejercicio_3():
    print("=== Ejercicio 3: Constructores ===")

    motor1 = Motor("283 CV", "Electrico")
    motor2 = Motor("150 CV", "Gasolina")

    coche1 = Coche("Tesla", "Model 3", 2024, motor1)
    coche2 = Coche("Mazda", "3", 2022, motor2)

    coche1.describir()
    print()

    coche2.describir()
    print()

# Prueba la herencia usando Vehiculo como clase base y Bicicleta como clase hija.
def ejercicio_4(): 
    print("=== Ejercicio 4: Herencia ===")

    vehiculo1 = Vehiculo()
    print(f"Velocidad inicial del vehiculo: {vehiculo1.velocidad} km/h")
    vehiculo1.acelerar()
    print(f"Velocidad actual del vehiculo: {vehiculo1.velocidad} km/h")
    print()

    bicicleta1 = Bicicleta("Montaña", 6)
    bicicleta1.describir()
    bicicleta1.acelerar()
    print(f"Velocidad actual de la bicicleta: {bicicleta1.velocidad} km/h")
    print()

# Prueba la sobreescritura y el polimorfismo con una lista de transportes.
def ejercicio_5_y_6():
    print("=== Ejercicio 5 y 6: Sobreescritura y Polimorfismo ===")

    motor1 = Motor("180 CV", "Gasolina")
    coche1 = Coche("Ford", "Focus", 2020, motor1)
    bicicleta1 = Bicicleta("Ruta", 8)

    transportes = [coche1, bicicleta1]

    for transporte in transportes:
        transporte.describir()
        transporte.acelerar()
        print(f"Velocidad actual: {transporte.velocidad} km/h")
        print()

#Prueba clases abstractas 
def ejercicio_7():
    print("Clases abstractas: ")
    perro1 = Perro()
    gato1 = Gato()

    animales = [perro1, gato1]

    for animal in animales:
        animal.hacerSonido()


# Prueba la composición creando un coche que contiene un objeto Motor.
def ejercicio_9():
    print("=== Ejercicio 9: Composicion ===")

    motor1 = Motor("283 CV", "Electrico")
    coche1 = Coche("Tesla", "Model 3", 2024, motor1)

    coche1.describir()
    coche1.acelerar()
    print(f"Velocidad actual: {coche1.velocidad} km/h")
    print()

# Prueba la excepción personalizada cuando el coche supera la velocidad permitida.
def ejercicio_10():
    print("=== Ejercicio 10: Excepciones ===")

    motor1 = Motor("120 CV", "Gasolina")
    coche1 = Coche("Ford", "Focus", 2020, motor1)

    try:
        coche1.incrVelocidad(250)
    except ExcesoVelocidadException as e:
        print(e)

    print()

# Ejecuta todos los ejercicios en el orden en que se han trabajado.
def main():
    ejercicio_1()
    ejercicio_2()
    ejercicio_3()
    ejercicio_4()
    ejercicio_5_y_6()
    ejercicio_7()
    ejercicio_8()
    ejercicio_9()
    ejercicio_10()

# Inicia la ejecución principal del archivo.
main()
