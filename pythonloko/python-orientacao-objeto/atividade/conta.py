class Conta():

    def __init__(self,numero_conta,cpf_conta,saldo,limite,nome):
        self.numero_conta = numero_conta
        self.cpf_conta = cpf_conta
        self.saldo = saldo
        self.limite = limite
        self.nome = nome
        print(f'\nConta criada com sucesso,Sr.{nome}\n')

    def Sacar(self,v):
        self.saldo -= v
        if self.saldo < 0:
            devendo = self.saldo * -1
            print(f'\nVoce esta devendo: R${devendo}\n')

    def Depositar(self,v):
        if v + self.saldo > self.limite:
            resp = v + self.saldo - self.limite
            print(f'\nVoce excedeu R${resp} o seu limite e de R${self.limite}\nFoi devolvido ao Sr.{self.nome} R${resp}')
            self.saldo = self.saldo + v - resp
        else:
            self.saldo += v