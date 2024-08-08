''''
Exercicio: Crie um software de gerenciamento bancario
esse software podera ser capaz de criar clientes e contas
cada cliente possui nome,cpf,idade
cada conta possui 1 cliente, saldo, limite, sacar, depositar e consultar saldo
'''

from cliente import Cliente#serve para conseguir criar o cliente
from conta import Conta#serve para conseguir criar a conta
from colorama import Fore

#Linha para decorar
def linha(v):#cria uma funcao onde pede um valor para quando a iniciar
    print(Fore.BLUE + v*"-" + Fore.RESET)#mostra o caractere escolhido a quantidade do valor selecionado na funcao

lista_contas = []#lista onde ficara armazenado as contas
lista_clientes = []#lista onde ficara armazenado os clientes

linha(50)#linha decorativa
print('\n\tGerenciamento Bancario',
      '\nOla somos da empresa KITTBANCA fornecemos criacoes\n'
      'de contas e registros de clientes\n')#mostra informacoes sobre o banco e oq pode fazer.

def Criando_Cliente():#cria uma funcao chamada para criar um cliente
    nome = input('\nInsira o NOME do cliente: ')#pergunta o nome do cliente
    cpf = input('Insira o CPF do cliente: ')#pergunta o cpf do cliente
    idade = input('Insira a IDADE do cliente: ')#pergunta a idade do cliente
    print('')#linha vazia
    linha(50)#linha decorativa
    if nome != '' or cpf != '' or idade != '':#se as informacoes forem totalmente completas
        lista_clientes.append(Cliente(nome,cpf,idade))#cria o cliente e adiciona ele na lista de clientes
    else:#se as informacoes nao forem totalmente completas
        print('Informacoes erradas tente novamente')#mostrar que falta informacoes para serem preenchidas e fala para tentar novamente
def Criando_Conta(num_conta):#funcao chamada para criar a conta onde essa funcao pede um variavel que e o numero da conta
    if len(lista_clientes) == 0:#se o tamanho da lista for = 0
        print('\nVoce ainda nao tem um cliente, por favor faca um antes de criar a conta')#mostra que voce ainda nao tem um cliente e que para criar uma conta e nescessario um cliente
    else:#se a lista tiver algum cliente
        cpf_conta = input('\nInsira um Cpf para a conta: ')#pedir o cpf para a conta
        print('')#linha vazia
        linha(50)#linha deocrativa
        for cliente in lista_clientes:#para cada cliente na lista
            if cliente.cpf == cpf_conta:#conferir se o cpf do cliente e o msm cpf que foi inserido para criar a conta
                num_conta += 1#soma o numero da conta para nunca ser igual
                lista_contas.append(Conta(num_conta, cpf_conta, 0.00, 100.00,cliente.nome))#cria a conta com as informacoes e adiciona a conta na lista de contas
            elif cliente.cpf != lista_clientes:#se o cpf inserido nao existir nenhum cliente com o cpf
                print('Cliente inexistente')#mostrar que nao existe um cliente com o cpf indicado

while True:#enquanto True for True
    linha(50)#linha decorativa
    print(f'\n{Fore.BLUE}1-{Fore.RESET} Cadastrar Cliente\n{Fore.BLUE}2-{Fore.RESET} Cadastrar Conta\n{Fore.BLUE}3-{Fore.RESET} Movimentar conta\n{Fore.BLUE}4-{Fore.RESET} Consultar Conta\n{Fore.BLUE}5-{Fore.RESET} Sair\n')#mostrar as opcoes que existem no programa
    linha(50)#linha decorativa
    opcao = input('\nSelecione: ')#pergunta qual das opcoes acima o cliente escolhe fazer
    print('')#linha vazia
    linha(50)#linha decorativa
    if opcao == '1':#se a opcao escolhida for a opcao 1
        Criando_Cliente()#chama a funcao para criar o cliente
    elif opcao == '2':#se a opcao escolhida for a opcao 2
        Criando_Conta(0)#chama a funcao para criar a conta, passando o numero inicial de conta
    elif opcao == '3':#se a opcao escolhida for a opcao 3
        print('\tMovimentacao de Conta')#mostra o titulo 
        linha(50)#linha decorativa
        cpf_consulta = input('\nInforme o CPF da conta: ')#pede um cpf para consultar nesse caso consultar para ver se existe uma conta
        print('')#linha vazia
        linha(50)#linha decorativa
        for conta in lista_contas:#para cada conta na lista de contas
            if cpf_consulta == conta.cpf_conta:#se o cpf inserido for igual ao cpf de alguma conta
                saida_cliente = ''#nome do cliente
                saida_numero = 0#numero da conta
                saida_saldo = 0.00#saldo da conta
                saida_limite = 0.00#limite da conta
                valor = 0.00#uma variavel onde vc mudara o valor, vc ira inserir um valor para depositar ou sacar.
                for cliente in lista_clientes:#para cada cliente na lista de clientes
                    if cliente.cpf == cpf_consulta:#se o cpf do cliente for o msm que o cpf inserido
                        saida_cliente = cliente.nome#armazenando o nome do cliente na variavel
                for conta in lista_contas:#para cada conta na lista de contas
                    if conta.cpf_conta == cpf_consulta:#se o cpf da conta for o msm que o cpf inserido
                        saida_numero = conta.numero_conta#armazenando o numero da conta na variavel
                        saida_saldo = conta.saldo#armazenando o saldo da conta na variavel
                        saida_limite = conta.limite#armazenando o limite da conta na variavel
                        print(f"\nNome: {saida_cliente}\nConta: {saida_numero}"
                              f"\nSaldo: R$ {saida_saldo:.2f}\nLimite: R$ {saida_limite:.2f}\n")#mostra as informacoes da conta e nome do cliente
                        linha(50)#linha decorativa
                        print(f"\nDigite:\n{Fore.BLUE}1-{Fore.RESET} Sacar\n{Fore.BLUE}2-{Fore.RESET} Depositar\n")
                        linha(50)#linha decorativa
                        acao = input("\nEscolha:\n")#pergunta se o cliente deseja fazer um saque ou um deposito
                        valor = float(input("\nInforme o valor: R$"))#pergunta o valor que o cliente ira sacar ou depositar
                        print('')#linha vazia
                        linha(50)#liha decorativa
                        if acao == '1':#se for escolhido a opcao sacar
                            conta.Sacar(valor)#saca o valor inserido na conta
                            if conta.saldo > 0:
                                print(f'\nSeu saldo mudou: R${conta.saldo}\n')#mostra o quanto o saldo da conta
                        elif acao == '2':#se nao se for escolhido a opcao depositar
                            conta.Depositar(valor)#depositar o valor inserido para a conta
                            if conta.saldo > 0:#se o saldo da conta for maior que 0
                                print(f'\nSeu saldo mudou: R${conta.saldo}\n')#mostra o saldo atual
                            elif conta.saldo < 0:#se o saldo da conta for menor que 0
                                devendo = conta.saldo * -1#armazena o valor que esta devendo
                                if devendo + valor < 0:#se o valor de devendo mais o valor inserido for menor que zero
                                    print(f'\nVoce esta devendo: R${devendo}\n')#mostra o quando vc ainda esta devendo
                                else:#se o valor que esta devendo mais o valor inserido for maior que zero
                                    print(f'\nVoce parou de dever e seu saldo mudou: R${conta.saldo}\n')#mostra que voce parou de dever e mostra o saldo atual
                        else:#se nao for nenhuma opcao
                            print('Opcao invalida')#mostra que a opcao nao foi encontrada
            else:#se nao encontrar nenhuma cona com o cpf inserido
                print('Conta nao encontrada')#mostra que nao encontramos nenhuma conta
                linha(50)#linha decorativa
        if len(lista_contas) == 0:#se o nao tiver nenhuma conta na lista de contas
            print('Conta nao encontrada')#mostrar que a conta nao foi encontrada
    elif opcao == '4':#se a opcao escolhida for 4
        cpf_consulta = input('\nInforme o CPF da conta: ')#pergunta o cpf da conta
        print('')#linha vazia
        linha(50)#linha decorativa
        for conta in lista_contas:#para cada conta na lista de contas
            if conta.cpf_conta == cpf_consulta:#se o cpf da conta for igual ao cpf inserido
                saida_cliente = ''#nome do cliente
                saida_numero = 0#numero da conta
                saida_saldo = 0.00#saldo da conta
                saida_limite = 0.00#limite da conta

                for cliente in lista_clientes:#para cada cliente na lista de clientes
                    if cliente.cpf == cpf_consulta:#se o cpf do cliente for igual ao cpf inserido
                        saida_cliente = cliente.nome#armazena o nome do cliente na variavel
                for conta in lista_contas:#para cada conta na lista de contas
                    if conta.cpf_conta == cpf_consulta:#se o cpf da conta for igual ao cpf inserido
                        saida_numero = conta.numero_conta#armazena o numero da conta na variavel
                        saida_saldo = conta.saldo#armazena o saldo da conta na variavel
                        saida_limite = conta.limite#armazena o limite da conta na variavel
                print(f"\nNome: {saida_cliente}\nConta: {saida_numero}"
                      f"\nSaldo: R$ {saida_saldo:.2f}\nLimite: R$ {saida_limite:.2f}\n")#mostra os detalhes,tipo: nome, numero da conta, saldo e limite
            else:#se nao encontar nenhum
                print('\nConta ou Cliente nao encontrado\n')#mostrar que nao foi encontrado a conta nem o cliente com o cpf inserido
    elif opcao == '5':#se nao se a opcao escolhida for 5
        break#quebrar
    else:#se nao achar nenhuma opcao
        print('Opcao Invalida...')#mostrar que a opcao foi invalida
print('\nFim do programa\n')#mostrar que o programa foi finalizado com sucesso
linha(50)#linha decorativa