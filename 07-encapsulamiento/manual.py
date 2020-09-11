class CasillaDeVotacion:

    def __init__(self, identificador, pais):
        
        self.__identificador = identificador
        self.__pais = pais
        self.__region = None

    def get_region(self):
        return self.__region
    
    def set_region(self, region):
        if region in self.__pais:
            self.__region = region
        else:
            raise ValueError(f'La región {region} no está en la lista')

if __name__ == '__main__':
    casilla = CasillaDeVotacion(1, ['Cancún','Mérida', 'Morelos'])
    print(casilla.get_region())
    casilla.set_region('Mérida')
    print(casilla.get_region())