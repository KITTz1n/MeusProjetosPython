class Cliente:#cria uma classe chamada Cliente

    def __init__(self, nome, cpf, idade):#funcao init para quando chamar a classe Conta pedir variaveis: nome do cliente, cpf do cliente, idade do cliente
        self.nome = nome#armazena na classe o nome do cliente
        self.cpf = cpf#armazena na classe o cpf do cliente
        self.idade = idade#armazena na classe a idade do cliente
        print(f'\nMuito obrigado Sr.{nome} seu cliente foi\nregistrado com sucesso\n')#mostra que o cliente foi registrado com sucesso