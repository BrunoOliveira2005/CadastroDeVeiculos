from veiculo import veiculo

class caminhao(veiculo):
    def __init__(self, marca, modelo, placa, ano, capacidade):
        super().__init__(marca, modelo, placa, ano)
        self.__capacidade = capacidade

    def __str__(self):
        return super().__str__() + f"    Capacidade: {self.__capacidade}"

    def getCapacidade(self):
        return self.__capacidade()