class CasillaDeVotacion:
    
    def __init__(self, identificador, pais):
        
        self.__identificador = identificador
        self.__pais = pais
        self.__region = None

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, region):
        if region in self.__pais:
            self.__region = region
        else:
            raise ValueError(f'La region {region} no esta en la lista')


if __name__ == '__main__':
    casilla = CasillaDeVotacion(123,['Cancún','Mérida', 'Morelos'])
    print(casilla.region)
    casilla.region = 'Mérida'
    print(casilla.region)