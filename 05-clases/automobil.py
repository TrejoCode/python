class Automovil:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estatus = "Encendido"
        self._motor = Motor(cilindros = 4)

    def acelerar(self, tipo = "despacio"):

        if tipo == "rapido":
            self._motor.injectar(20)
        else:
            self._motor.injectar(10)

        self._estatus = "Movimiento"

class Motor:

    def __init__(self, cilindros, tipo = "Gasolina"):
        self.cilindros = cilindros
        self.tipo = tipo
        self.temperatura = 0

    def injectar(self, cantidad):
        pass