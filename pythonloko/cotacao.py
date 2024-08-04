import json
import requests
from colorama import Fore

#Biblioteca

class Cotacao:

    def __init__(self):
        pass

    def dicionario(self):
        req = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
        dicionario = json.loads(req.text)
        return dicionario

    def dolar(self,dic):
        self.resp1 = dic['USDBRL']
        self.dolar_real_compra = float(self.resp1['bid'])
        self.dolar_real_venda = float(self.resp1['bid'])
        self.data_dolar = self.resp1['create_date']
        lista_dlr = [self.dolar_real_compra,self.dolar_real_venda,self.data_dolar]
        return lista_dlr
    def euro(self,dic):
        self.resp2 = dic['EURBRL']
        self.euro_real_compra = float(self.resp2['bid'])
        self.euro_real_venda = float(self.resp2['bid'])
        self.data_euro = self.resp2['create_date']
        lista_eur = [self.euro_real_compra, self.euro_real_venda, self.data_euro]
        return lista_eur
    def bitcoin(self,dic):
        self.resp3 = dic['BTCBRL']
        self.btc_real_compra = float(self.resp3['bid'])
        self.btc_real_venda = float(self.resp3['bid'])
        self.data_btc = self.resp3['create_date']
        lista_btc = [self.btc_real_compra, self.btc_real_venda, self.data_btc]
        return lista_btc
    def printar(self,linha,dlr_c,dlr_v,dlr_d,eur_c,eur_v,eur_d,btc_c,btc_v,btc_d):
        print(Fore.BLUE + linha * '-' + Fore.RESET)
        print('\n\t\t\tKITTcota'
              '\nSomos um programa de cotacoes onde temos a cotacao\n'
              'do dolar,euro e bitcoin para real.\n')
        print(Fore.BLUE + linha * '-' + Fore.RESET)
        print('\n1- Dolar  3- Bitcoin\n2- Euro   4- Sair\n')
        print(Fore.BLUE + linha * '-' + Fore.RESET)
        op = input('\nEscolha uma das opcoes:\n')
        print('')
        print(Fore.BLUE + linha * '-' + Fore.RESET)
        if op == '1':
            print('\n\t\t\t\033[1mDolar\033[0m')
            print(f'\nValor em dolar: U$1.00\nValor em reais de compra: R${dlr_c:.2f}'
                  f'\nValor em reais de venda: R${dlr_v:.2f}\nData: {dlr_d}\n')
        elif op == '2':
            print(f'\nValor em Euro: €1.00\nValor em reais de compra: R${eur_c:.2f}'
                  f'\nValor em reais de venda: R${eur_v:.2f}\nData: {eur_d}\n')
        elif op == '3':
            print(f'\nValor em Bitcoin: ₿1.00\nValor em reais de compra: R${btc_c:.2f}'
                  f'\nValor em reais de venda: R${btc_v:.2f}\nData: {btc_d}\n')
        elif op == '4':
            print('\nOkay!')
            print(Fore.BLUE + linha * '-' + Fore.RESET)
            exit()
        else:
            print('Nao achamos essa opcao, Tente novamente!')