from aula9.veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, cor, marca, tanque, quant_litro_max):
        Veiculo.__init__(self, cor, 4, marca, tanque, quant_litro_max)
    #Heranca entre classe acontecendo acima