''''
faca um programa onde ele mostre em tempo real a cotacao do dolar
'''

import requests

dicionario = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')


print(dicionario.text)