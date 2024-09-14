class Veiculo:

    def __init__(self, cor, rodas, marca, tanque, quant_litro_max):
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque
        self.quant_litro_max = quant_litro_max
        self.excedeu = ''
        self.quant_gasto = ''

    def abastecer(self, litros):
        if self.tanque <= self.quant_litro_max:
            self.tanque += litros
            if self.tanque > self.quant_litro_max:
                self.excedeu = self.tanque - self.quant_litro_max
                self.tanque = self.tanque - self.excedeu
            print('Tanque Abastecido')
        else:
            print('Tanque ja esta cheio')
    def andar(self, quant_km, gasto):
        self.quant_gasto = gasto*quant_km
        self.tanque -= self.quant_gasto
