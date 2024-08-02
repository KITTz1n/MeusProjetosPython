''''
Exercicio: Crie um software de gerenciamento bancario
esse software podera ser capaz de criar clientes e contas
cada cliente possui nome,cpf,idade
cada conta possui 1 cliente, saldo, limite, sacar, depositar e consultar saldo
'''

from atividade.cliente import Cliente
from atividade.conta import Conta

#Linha para decorar
def linha(tamanho):
    print(tamanho*"-")

lista_contas = []
lista_clientes = []
a = 0

linha(50)
print('\tGerenciamento Bancario',
      '\nOla somos da empresa KITTBANCA fornecemos criacoes\n'
      'de contas e registros de clientes',)

def Criando_Cliente():
    #precisa perguntar nome,cpf,idade e armazena-los
    nome = input('Insira o NOME do cliente: ')
    cpf = input('Insira  o CPF do cliente: ')
    idade = input('Insira a IDADE do cliente: ')
    linha(50)
    if nome != '' and cpf != '' and idade != '':
        lista_clientes.append(Cliente(nome,cpf,idade))
        print(lista_clientes)
    else:
        print('Informacoes erradas tente novamente')
def Criando_Conta(num_conta):
    if len(lista_clientes) == 0:
        print('Voce ainda nao tem um cliente, por favor faca um antes de criar a conta')
    else:
        cpf_conta = input('Insira um Cpf para a conta:')
        for cliente in lista_clientes:
            if cliente.cpf == cpf_conta:
                num_conta += 1
                lista_contas.append(Conta(num_conta, cpf_conta, 0.00, 100.00,cliente.nome))
            elif cliente.cpf != lista_clientes:
                print('Cliente inexistente')

while True:
    linha(50)
    print('\n1- Cadastrar Cliente\n2- Cadastrar Conta\n3- Movimentar conta\n4- Consultar Conta\n5- Sair\n')
    linha(50)
    opcao = input('\nSelecione: ')
    print('')
    linha(50)
    if opcao == '1':
        Criando_Cliente()
    elif opcao == '2':
        Criando_Conta(0)
    elif opcao == '3':
        print('\tMovimentacao de Conta')
        linha(50)
        cpf_consulta = input('\nInforme o CPF da conta: ')
        linha(50)
        for conta in lista_contas:
            if cpf_consulta == conta.cpf_conta:
                saida_cliente = ''
                saida_numero = 0
                saida_saldo = 0.00
                saida_limite = 0.00
                valor = 0.00
                for cliente in lista_clientes:
                    if cliente.cpf == cpf_consulta:
                        saida_cliente = cliente.nome
                for conta in lista_contas:
                    if conta.cpf_conta == cpf_consulta:
                        saida_numero = conta.numero_conta
                        saida_saldo = conta.saldo
                        saida_limite = conta.limite
                        print(f"Nome: {saida_cliente}\nConta: {saida_numero}"
                              f"\nSaldo: R$ {saida_saldo:.2f}\nLimite: R$ {saida_limite:.2f}")
                        valor = float(input("Informe o valor: R$"))
                        acao = input("Digite 1 - Sacar\nDigite 2 - Depositar:")
                        if acao == '1':
                            conta.Sacar(valor)
                            print(f'Seu Saldo Mudou: R${conta.saldo}')
                        elif acao == '2':
                            conta.Depositar(valor)
                            print(f'Seu Saldo Mudou: R${conta.saldo}')
                            if conta.saldo < 0:
                                devendo = conta.saldo * -1
                                print(f'Voce esta devendo: R${devendo}')
                        else:
                            print('Opcao invalida')
                        linha(50)
            else:
                print('Conta nao encontrada')
                linha(50)
        if len(lista_contas) == 0:
            print('Conta nao encontrada')
    elif opcao == '4':
        cpf_consulta = input('Informe o CPF da conta: ')
        for conta in lista_contas:
            if conta.cpf_conta == cpf_consulta:
                saida_cliente = ''
                saida_numero = 0
                saida_saldo = 0.00
                saida_limite = 0.00

                for cliente in lista_clientes:
                    if cliente.cpf == cpf_consulta:
                        saida_cliente = cliente.nome
                for conta in lista_contas:
                    if conta.cpf_conta == cpf_consulta:
                        saida_numero = conta.numero_conta
                        saida_saldo = conta.saldo
                        saida_limite = conta.limite
                print(f"Nome: {saida_cliente}\nConta: {saida_numero}"
                      f"\nSaldo: R$ {saida_saldo:.2f}\nLimite: R$ {saida_limite:.2f}")
            else:
                print('Cliente nao encontrado')
    elif opcao == '5':
        break
    else:
        print('Opcao Invalida...')

print('Fim do programa')