'''
Exercicio: faca um programa que leia a quantidade de
pessoas que serao convidadas para uma festa.
apos isso o programa ira perguntar o nome de todas as pessoas
e colocar numa lista de convidados.
apos isso ira imprimir todos os nomes da lista
'''

print('\t\tConvites')
lista_conv_nomes = []
quant_conv = int(input('Digite quantos convidados seram chamados: '))
contador = 0

print('\nOkay, Escreva quem sera convidado\n')
while quant_conv > 0:
    nomes = input('Digite um nome:')
    lista_conv_nomes.append(nomes)
    quant_conv -= 1
    contador +=1

print('\n\tLista de Convidados')
for nome in lista_conv_nomes:
    print('Foi Convidado:',nome)
print('Quantidade de convidados:', contador)