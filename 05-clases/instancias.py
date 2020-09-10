class Coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otro_cordenada):
        x_diff = (self.x - otro_cordenada.x)**2
        y_diff = (self.y - otro_cordenada.y)**2

        return (x_diff + y_diff)**0.5
    
if __name__ == '__main__':
    coord1 = Coordenada(3,30)
    coord2 = Coordenada(4,40)

    print(coord1.distancia(coord2))