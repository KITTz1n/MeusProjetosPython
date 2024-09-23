#Calculadora

from calculos import Calculos#serve para catar o sistema de contas
from colorama import Fore#serve para colorir as linhas decorativas

def linha(v):#inicia uma funcao onde pede um valor para V
    print(Fore.BLUE + v * '-' + Fore.RESET)#mostra '-' com a quantidade sendo o valor de V, fazendo uma linha decorativa e colorindo ela dps

linha(50)#linha decorativa

while True:#sempre que true for true

    print(f'\n\t\t{Fore.BLUE}Calculadora{Fore.RESET}\n\n{Fore.BLUE}1-{Fore.RESET} Soma\n{Fore.BLUE}2-{Fore.RESET} Subtracao\n{Fore.BLUE}3-{Fore.RESET} Multiplicacao\n{Fore.BLUE}4-{Fore.RESET} Divisao\n{Fore.BLUE}5-{Fore.RESET} Sair\n')#mostrar o titulo e as 5 opcoes de escolhas sendo elas: Soma, Subtracao, Multiplicacao, Divisao e Sair.
    linha(50)#linha decorativa
    sinal = input('\nOque voce deseja fazer?\n')#perguntando a escolha do cliente entre as opcoes acima
    print('')#linha vazia
    linha(50)#linha decorativa

    if sinal == '1':#se a escolha for 1
        print(f'\n\t\t{Fore.BLUE} Soma{Fore.RESET}\n')#mostra o titulo que nesse caso se chama Soma.
        valor = Calculos.soma(Calculos.pergunta(),Calculos.pergunta())#pergunta dois valores e calcula a soma do valor1 e valor2 e armazena o resultado na variavel 'valor'.
        print(f'\n\t{Fore.BLUE}    Resultado:{Fore.RESET}',valor,'\n')#mostra o resultado que esta na variavel 'valor'.
        linha(50)#linha decorativa.
    elif sinal == '2':#se nao se a escolha for 2.
        print(f'\n\t\t{Fore.BLUE} Subtracao{Fore.RESET}\n')#mostra o titulo que nesse caso se chama Subtracao.
        valor = Calculos.subtracao(Calculos.pergunta(),Calculos.pergunta())#pergunta dois valores e calcula a subtracao do valor 1 e valor 2 e armazena o resultado na variavel 'valor'.
        print(f'\n\t{Fore.BLUE}    Resultado:{Fore.RESET}',valor,'\n')#mostra o resultado que esta na variavel 'valor'.
        linha(50)#linha decorativa.
    elif sinal == '3':#se nao se a escolha for 3.
        print(f'\n\t\t{Fore.BLUE} Multiplicacao{Fore.RESET}\n')#motra o titulo que nesse caso se chama Multiplicacao.
        valor = Calculos.multiplicacao(Calculos.pergunta(),Calculos.pergunta())#pergunta dois valores e calcula a multiplicacao do valor 1 e valor 2 e armazena o resultado na variavel 'valor'.
        print(f'\n\t{Fore.BLUE}    Resultado:{Fore.RESET}',valor,'\n')#mostra o resultado que esta na variavel 'valor'.
        linha(50)#linha decorativa.
    elif sinal == '4':#se nao se a escolha for 4
        print(f'\n\t\t{Fore.BLUE} Divisao{Fore.RESET}\n')#mostra o titulo que nesse caso se chama Divisao.
        valor = Calculos.divisao(Calculos.pergunta(),Calculos.pergunta())#pergunta dois valores e calcula a divisao do valor 1 e valor 2 e armazena o resultado na variavel 'valor'.
        print(f'\n\t{Fore.BLUE}    Resultado:{Fore.RESET}',valor,'\n')#mostra o resultado que esta na variavel 'valor'.
        linha(50)#linha decorativa.
    elif sinal == '5':#se nao se a escolha for 5
        print('\nSaindo...\n')#mostrar que esta saindo do programa
        break#sair do loop infinito
    else:#se a escolha nao for nenhuma das opcoes
        print('\nOpcao Invalida, tente novamente\n')#mostrar que a opcao que foi inserido e invalida
        linha(50)#linha decorativa
linha(50)#linha decorativa