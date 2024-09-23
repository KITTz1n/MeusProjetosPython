class Conta():#cria uma classe chamada Conta

    def __init__(self,numero_conta,cpf_conta,saldo,limite,nome):#funcao init para quando chamar a classe Conta pedir variaveis: num,cpf,saldo,limite da conta e o nome do cliente
        self.numero_conta = numero_conta#armazena na classe o numero da conta
        self.cpf_conta = cpf_conta#armazena na classe o cpf da conta
        self.saldo = saldo#armazena na classe o saldo da conta
        self.limite = limite#armazena na classe o limite da conta
        self.nome = nome#armazena na classe o nome do cliente que criou a conta
        print(f'\nConta criada com sucesso,Sr.{nome}\n')#mostra que a conta foi criada com sucesso

    def Sacar(self,v):#funcao de sacar para quando dentro da classe chama-la e ela pede um valor que nesse caso e o valor de V
        self.saldo -= v#faz subtrai V(valor inserido na funcao) de saldo
        if self.saldo < 0:#se o saldo for menor que zero
            devendo = self.saldo * -1#calcula o numero que vc deve
            print(f'\nVoce esta devendo: R${devendo}\n')#mostra o quando vc esta devendo atualmete

    def Depositar(self,v):#funcao de depositar para quando dentro da classe chama-la e ela pede um valor que nesse caso e o valor de V
        if v + self.saldo > self.limite:#se a soma de V(valor inserido na funcao) com o saldo atual da conta for maior que o limite da conta
            resp = v + self.saldo - self.limite#calcular o excesso de deposito
            print(f'\nVoce excedeu R${resp} o seu limite e de R${self.limite}\nFoi devolvido ao Sr.{self.nome} R${resp}')#mostra a quantidade excedida, mostra o limite e a quantidade devolvida
            self.saldo = self.saldo + v - resp#calcula a soma do saldo com o V(valor inserido na funcao) menos o valor de excesso do deposito
        else:#se nao exceder
            self.saldo += v#somar o saldo com o V(valor inserido na funcao)