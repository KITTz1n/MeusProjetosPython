#Metodos e funcoes
var1 = int(input('Coloque um numero para ser somado: '))
var2 = int(input('Coloque outro: '))

def soma(numero1,numero2):
    resposta = numero1+numero2
    return resposta  

retorno = soma(var1,var2)
print(retorno)

def imprimi_oi():# <-metodo
    print('Oi')
imprimi_oi()

def tem_quatro_itens(x):
    if len(x) == 4:
        print('Tem 4 itens')
    else:
        print('Nao tem 4 itens')
tem_quatro_itens([1,2,3,4])