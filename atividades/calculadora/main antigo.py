#Calculadora

print('\n\t\tCalculadora')

sinal = input('Voce quer fazer uma conta com qual sinal? escreva por extenso: ')

#Funcoes
def soma(numero1,numero2):
    resp = numero1+numero2
    return resp
def subtracao(numero1,numero2):
    resp = numero1-numero2
    return resp
def multiplicacao(numero1,numero2):
    resp = numero1*numero2
    return resp
def divisao(numero1,numero2):
    resp = numero1/numero2
    return resp

#Numeros

if sinal == 'mais':
    print('\tSoma')
    num1 = float(input('Escreva algum numero:'))
    num2 = float(input('Escreva outro numero:'))

    print(soma(num1,num2))

elif sinal == 'menos':
    print('\tSubtracao')
    num1 = float(input('Escreva algum numero:'))
    num2 = float(input('Escreva outro numero:'))

    print(subtracao(num1,num2))

elif sinal == 'multiplicacao':
    print('\tMultiplicacao')
    num1 = float(input('Escreva algum numero:'))
    num2 = float(input('Escreva outro numero:'))

    print(multiplicacao(num1,num2))

elif sinal == 'divisao':
    print('\tDivisao')
    num1 = float(input('Escreva algum numero:'))
    num2 = float(input('Escreva outro numero:'))

    print(divisao(num1,num2))
else:
    print('Sinal Invalido')