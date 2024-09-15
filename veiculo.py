class veiculo: 
    # __init_ => é o método construtor
    def __init__(self, marca, modelo, placa, ano):
        #Métodos privados (Encapsulamento)
        self.__marca = marca
        self.__modelo = modelo
        self.__placa = placa
        self.__ano = ano

    def __str__(self):
        return f'''
            Marca: {self.__marca}
            Modelo: {self.__modelo}
            Placa: {self.__placa}
            Ano: {self.__ano}        
        '''

    # Método de instância
    def calcularTempoUso(self):
        return 2024 - self.ano

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

    def getPlaca(self):
        return self.__placa

    def getAno(self):
        return self.__ano