from colorama import Fore,Style

def linhas(v):

    print(Fore.BLUE + v * '-' + Fore.RESET)

def conta(a,b,c,digite):
    
    try:
        part1 = b*b
        part2 = 4*a*c

        delta = part1 - part2

        part3 = delta**(1/2)
        part4 = 2*a

        x1 = -(b) + part3
        respX1 = x1/part4

        x2 = -(b) - part3
        respX2 = x2/part4

        print(f'\n\t\t{Fore.BLUE+Style.BRIGHT}{digite}{Fore.RESET+Style.NORMAL}')
        print(f'\n{Fore.BLUE}A:{Fore.RESET} {a}\n{Fore.BLUE}B:{Fore.RESET} {b}\n{Fore.BLUE}C:{Fore.RESET} {c}\n')
        print(f'{Fore.BLUE}Delta:{Fore.RESET} {delta}')
        print(f'{Fore.BLUE}x1 ≃{Fore.RESET} {respX1:.1f}')
        print(f'{Fore.BLUE}x2 ≃{Fore.RESET} {respX2:.1f}\n')
    except ZeroDivisionError:
        print(f'\n\t\t{Fore.BLUE+Style.BRIGHT}{digite}{Fore.RESET+Style.NORMAL}')
        print(f'\n{Fore.BLUE}A:{Fore.RESET} {a}\n{Fore.BLUE}B:{Fore.RESET} {b}\n{Fore.BLUE}C:{Fore.RESET} {c}\n')
        print(f'{Fore.BLUE}Delta:{Fore.RESET} {delta}')
        print(f'\n{Fore.BLUE}Erro:{Fore.RESET} Divisao por zero, na formula:\n\n\t{b*-1} +- {part3:.0f}\n\t{Fore.BLUE}-------{Fore.RESET}\n\t 2 * {a}\n')

def definindo_abc(texto):
    try:

            espliti = texto.split('x')
            var2 = f'{espliti[1]}{espliti[2]}'
            var3 = var2.split(' ')
            var4 = f'{espliti[0]}'
            var5 = var4.split(' ')
            if var5[0] == '':
                var.insert(0,1)
            elif var5[0] != '-':
                var.insert(0,int(var5[0]))
            if var5[0] == '-':
                if len(var5) > 1:
                    var.insert(0,int(var5[1])*-1)
                elif len(var5) == 1:
                    var.insert(0,-1)
            if var3[1] == '+':
                var.insert(1,int(var3[2]))
            elif var3[1] == '-':
                var.insert(1,int(var3[2])*-1)
            if var3[3] == '+':
                var.insert(2,int(var3[4]))
            elif var3[3] == '-':
                var.insert(2,int(var3[4])*-1)
    except:
        var.append(' ')

while True:
    var = []
    linhas(50)
    digite = input('\nDigite Uma Conta De Segundo Grau: ')
    print('')
    linhas(50)
    if digite == 'sair':
        print('\nPrograma finalizado\n')
        linhas(50)
        exit()
    while len(var) < 4:
        definindo_abc(digite)
    if var[0] != ' ':
        conta(var[0],var[1],var[2],digite)
    elif var[0] == ' ':
        print('\nErro, Tente Novamente!\n')