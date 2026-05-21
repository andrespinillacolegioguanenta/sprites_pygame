# Definición de la clase vehículo
class Vehiculo:

    # Constructor de la clase Veniculo
    def __init__(self, matricula, color, numeropuertas):
        self.MATRICULA = matricula
        self. COLOR = color
        self. NUMERO = numeropuertas
        self.AVANZA = False
        print ("Constucción de un vehículo : " + self. MATRICULA)
    # Metodo Avanzar
    def Avanzar(self):
        self.AVANZA = True
        print(self.MATRICULA + " avanza. ")
    # Metodo Detenerse
    def Detenerse(self):
        self. AVANZA = False
        print (self. MATRICULA + " se detiene.")

# Construcción de una primera instancia
vehiculo1 = Vehiculo("AR123", "rojo", 3)


# Construccion de una segunda instancia 
vehiculo2 = Vehiculo("FR456", "verde", 5)


# El primer vehiculo avanza
vehiculo1.Avanzar()


# El primer vehículo se detiene
vehiculo1.Detenerse()