''''
faca um programa onde ele mostre em tempo real a cotacao do dolar
'''

from cotacao import Cotacao

linha = 50

cot = Cotacao()
dic = cot.dicionario()
dlr = cot.dolar(dic)
eur = cot.euro(dic)
btc = cot.bitcoin(dic)

while True:
    cot.printar(linha,dlr[0],dlr[2],eur[0],eur[2],btc[0],btc[2])