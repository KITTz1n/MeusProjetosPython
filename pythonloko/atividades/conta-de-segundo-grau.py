sinal = 'nulo ou mais'

def linhas(v):
    print(v*'-')
while True:
    var = []
    linhas(50)
    digite = input('\ndigite uma conta de segundo grau: ')
    teste = digite.split(' ')
    print(teste)
    print(digite.split('x'))
    print('')
    linhas(50)
    if digite == 'sair':
        print('Programa finalizado')
        exit()
    for i in digite.split('x'):
        try:
            print(var)
            int(i)
            var.append(int(i))
            #if sinal == 'menos':
            #    var.append(int(i)*-1)
            #if sinal != 'menos':
            #    var.append(int(i))
        except:
            if i == '-':
                sinal = 'menos'
            else:
                sinal = 'nulo ou mais'
    a = var[0]
    b = var[1]
    c = var[2]

    part1 = b*b
    part2 = 4*a*c

    delta = part1 - part2

    part3 = delta**(1/2)
    part4 = 2*a

    x1 = -(b) + part3
    respX1 = x1/part4

    x2 = -(b) - part3
    respX2 = x2/part4

    print(f'\n\t{digitze}')
    print(f'\nA: {a}\nB: {b}\nC: {c}\n')
    print(f'Delta: {delta}')
    print(f'x1 ≃ {respX1:.1f}')
    print(f'x2 ≃ {respX2:.1f}\n')