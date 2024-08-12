#Bibliotecas necessarias

import json
import requests
from colorama import Fore,Style

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
    def printar(self,linha,dlr_c,dlr_d,eur_c,eur_d,btc_c,btc_d):
        print(Fore.BLUE + linha * '-' + Fore.RESET)
        print(f'\n\t\t{Style.BRIGHT+Fore.BLUE}KITTcota\n{Style.NORMAL+Fore.RESET}'
              '\nSomos um programa de cotacoes onde temos a cotacao\n'
              'do dolar,euro e bitcoin para real.\n')
        print(Fore.BLUE + linha * '-' + Fore.RESET)
        print(f'\n\t{Fore.BLUE}1-{Fore.RESET} Dolar  {Fore.BLUE}3-{Fore.RESET} Bitcoin\n\t{Fore.BLUE}2-{Fore.RESET} Euro   {Fore.BLUE}4-{Fore.RESET} Sair\n')
        print(Fore.BLUE + linha * '-' + Fore.RESET)
        print(f'\n\t\t{Style.BRIGHT+Fore.BLUE}Informacoes{Style.NORMAL+Fore.RESET}')
        op = input('\nEscolha uma das opcoes:\n')
        try:
            if int(op) < 4:
                quantia = float(input('\nQual a quantia:\n'))
        except:
            op = 'Error'
        print('')
        print(Fore.BLUE + linha * '-' + Fore.RESET)
        if op == '1':
            valor_c = dlr_c*quantia
            print(f'\n\t\t{Style.BRIGHT+Fore.BLUE}Dolar{Style.NORMAL+Fore.RESET}')
            print(f'\n{Fore.BLUE}Valor em dolar:{Fore.RESET} U${quantia}\n{Fore.BLUE}Valor em reais:{Fore.RESET} R${valor_c:.2f}'
                  f'\n{Fore.BLUE}Valor do dolar:{Fore.RESET} R${dlr_c:.2f}\n{Fore.BLUE}Data:{Fore.RESET} {dlr_d}\n')
        elif op == '2':
            valor_c = eur_c*quantia
            print(f'\n\t\t{Style.BRIGHT+Fore.BLUE}Euro{Style.NORMAL+Fore.RESET}')
            print(f'\n{Fore.BLUE}Valor em euro:{Fore.RESET} €{quantia}\n{Fore.BLUE}Valor em reais:{Fore.RESET} R${valor_c:.2f}'
                  f'\n{Fore.BLUE}Valor do euro:{Fore.RESET} R${eur_c:.2f}\n{Fore.BLUE}Data:{Fore.RESET} {eur_d}\n')
        elif op == '3':
            valor_c = btc_c*quantia 
            print(f'\n\t\t{Style.BRIGHT+Fore.BLUE}Bitcoin{Style.NORMAL+Fore.RESET}')
            print(f'\n{Fore.BLUE}Valor em bitcoin:{Fore.RESET} ₿{quantia}\n{Fore.BLUE}Valor em reais:{Fore.RESET} R${valor_c:.2f}'
                  f'\n{Fore.BLUE}Valor do bitcoin:{Fore.RESET} R${btc_c:.2f}\n{Fore.BLUE}Data:{Fore.RESET} {btc_d}\n')
        elif op == '4':
            print('\nOkay!\n')
            print(Fore.BLUE + linha * '-' + Fore.RESET)
            exit()
        else:
            print('\nNao achamos essa opcao, Tente novamente!\n')