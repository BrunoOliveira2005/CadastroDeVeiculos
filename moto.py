from veiculo import veiculo

#SubClasse (Herança)
class moto(veiculo):
    def __init__(self, marca, modelo, placa, ano, cilindradas):
        super().__init__(marca, modelo, placa, ano)
        self.__cilindradas = cilindradas

    def __str__(self):
        return super().__str__() + f'    Cilindradas: {self.__cilindradas}'
    
    def get_cilindradas(self):
        return self.__cilindradas