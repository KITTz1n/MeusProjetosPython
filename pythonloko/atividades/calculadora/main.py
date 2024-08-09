#Calculadora

from calculos import Calculos
from colorama import Fore

def linha(v):
    print(Fore.BLUE + v * '-' + Fore.RESET)


linha(50)

while True:

    print(f'\n\t\t{Fore.BLUE}Calculadora{Fore.RESET}\n\n{Fore.BLUE}1-{Fore.RESET} Soma\n{Fore.BLUE}2-{Fore.RESET} Subtracao\n{Fore.BLUE}3-{Fore.RESET} Multiplicacao\n{Fore.BLUE}4-{Fore.RESET} Divisao\n{Fore.BLUE}5-{Fore.RESET} Sair\n') 
    linha(50)
    sinal = input('\nVoce quer fazer uma conta com qual sinal?\n')
    print('')
    linha(50)

    if sinal == '1':
        try:
            print(f'\n\t\t{Fore.BLUE} Soma{Fore.RESET}\n')
            valor = Calculos.soma(Calculos.pergunta1(),Calculos.pergunta2())
            print(f'\n\t{Fore.BLUE}    Resultado:{Fore.RESET}',valor,'\n')
            linha(50)
        except:
            print('\nOpss! Tente novamente\n')
            linha(50)
    elif sinal == '2':
        try:
            print(f'\n\t\t{Fore.BLUE} Subtracao{Fore.RESET}\n')
            valor = Calculos.subtracao(Calculos.pergunta1(),Calculos.pergunta2())
            print(f'\n\t{Fore.BLUE}    Resultado:{Fore.RESET}',valor,'\n')
            linha(50)
        except:
            print('\nOpss! Tente novamente\n')
            linha(50)
    elif sinal == '3':
        try:
            print(f'\n\t\t{Fore.BLUE} Multiplicacao{Fore.RESET}\n')
            valor = Calculos.multiplicacao(Calculos.pergunta1(),Calculos.pergunta2())
            print(f'\n\t{Fore.BLUE}    Resultado:{Fore.RESET}',valor,'\n')
            linha(50)
        except:
            print('\nOpss! Tente novamente\n')
            linha(50)
    elif sinal == '4':
        try:
            print(f'\n\t\t{Fore.BLUE} Divisao{Fore.RESET}\n')
            valor = Calculos.divisao(Calculos.pergunta1(),Calculos.pergunta2())
            print(f'\n\t{Fore.BLUE}    Resultado:{Fore.RESET}',valor,'\n')
            linha(50)
        except:
            print('\nOpss! Tente novamente\n')
            linha(50)
    elif sinal == '5':
        print('\nSaindo...\n')
        break
    else:
        print('\nSinal Invalido, tente novamente\n')
        linha(50)
linha(50)