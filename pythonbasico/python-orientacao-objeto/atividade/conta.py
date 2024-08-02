import cliente
class Conta():
    def __init__(self,numero_conta,cpf_conta,saldo,limite,nome):
        self.numero_conta = numero_conta
        self.cpf_conta = cpf_conta
        self.saldo = saldo
        self.limite = limite
        print(f'\nConta criada com sucesso,Sr.{nome}')
    def Sacar(self,v):
        self.saldo -= v
        if self.saldo < 0:
            devendo = self.saldo * -1
            print(f'Voce esta devendo: R${devendo}')
    def Depositar(self,v):
        if v + self.saldo < self.limite:
            self.saldo += v
        else:
            resp = v + self.saldo - self.limite
            print(f'Voce excedeu {resp} o seu limite e de {self.limite}\nPor favor tente novamente')