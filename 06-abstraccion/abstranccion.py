class Lavadora:

    def __init__(self):
        pass

    def lavar(self, temperatura = "Caliente"):
        self.__llenar_tanque(temperatura)
        self.__enbajonar()
        self.__limpiar()
        self.__centrifugar()

    def __llenar_tanque(self, temperatura):
        print("Llenando lavadora")

    def __enbajonar(self):
        print("Enjabonando")

    def __limpiar(self):
        print("Lavando")

    def __centrifugar(self):
        print("Centrifugando")
    

if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()