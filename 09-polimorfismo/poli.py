## Nos permite definir nuestros métodos propios de cada clase, no es igual avanzar en general o avanzar en un área especializada
class Persona:

    def __init__(self, nombre):

        self.nombre = nombre

    def avanza(self):
        print("Me encuentro caminando")

class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print("Me muevo en bicicleta")

def run():
    persona = Persona("Sergio")
    persona.avanza()

    ciclista = Ciclista("Daniel")
    ciclista.avanza()

if __name__ == '__main__':
    run()