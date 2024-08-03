''''
faca um programa onde ele mostre em tempo real a cotacao do dolar
'''

import json
import requests
from colorama import Fore

def linha(v):
    print(Fore.BLUE+v*'-'+Fore.RESET)

req = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

dicionario = json.loads(req.text)

print(dicionario)

resp1 = dicionario['USDBRL']
resp2 = dicionario['EURBRL']
resp3 = dicionario['BTCBRL']

dolar_real_compra = float(resp1['bid'])
euro_real_compra = float(resp1['bid'])
btc_real_compra = float(resp1['bid'])

dolar_real_venda = float(resp1['bid'])
euro_real_venda = float(resp2['bid'])
btc_real_venda = float(resp3['bid'])

data_dolar = resp1['create_date']
data_euro = resp1['create_date']
data_btc = resp1['create_date']

while True:
      linha(50)
      print('\n\t\t\tKITTcota'
                 '\nSomos um programa de cotacoes onde temos a cotacao\n'
                 'do dolar,euro e bitcoin para real.\n')
      linha(50)
      print('\n1- Dolar  3- Bitcoin\n2- Euro   4- Sair\n')
      linha(50)
      op = input('\nEscolha uma das opcoes:\n')
      print('')
      linha(50)
      if op == '1':
            print(f'\nValor em dolar: U$1.00\nValor em reais de compra: R${dolar_real_compra:.2f}'
                  f'\nValor em reais de venda: R${dolar_real_venda:.2f}\nData: {data_dolar}\n')
      elif op == '2':
            print(f'\nValor em Euro: €1.00\nValor em reais de compra: R${euro_real_compra:.2f}'
                  f'\nValor em reais de venda: R${euro_real_venda:.2f}\nData: {data_euro}\n')
      elif op == '3':
            print(f'\nValor em Bitcoin: ₿1.00\nValor em reais de compra: R${btc_real_compra:.2f}'
                  f'\nValor em reais de venda: R${btc_real_compra:.2f}\nData: {data_btc}\n')
      elif op == '4':
            print('\nOkay!')
            exit()
      else:
            print('Nao achamos essa opcao, Tente novamente!')