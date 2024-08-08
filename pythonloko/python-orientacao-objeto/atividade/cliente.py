class Cliente:

    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        print(f'\nMuito obrigado Sr.{nome} seu cliente foi\nregistrado com sucesso\n')