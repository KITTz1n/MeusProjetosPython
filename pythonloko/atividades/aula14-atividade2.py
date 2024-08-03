''''
faca um programa que mostre em tempo real a previsao do tempo
'''

import json
import requests
from colorama import Fore,Style

apikey = 'bd52c47783991ed037de97c070ea65e8'
lang = 'pt_br'

def linha(v):
    print(Fore.BLUE+v*'-'+Fore.RESET)

while True:
    linha(50)

    nome_cidade = input('\nInsira o lugar que quer consultar o clima:\n')

    req = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={nome_cidade}&appid={apikey}&lang={lang}')

    dicionario = json.loads(req.text)

    try:
        nome = dicionario['name']
        tempo = dicionario['weather'][0]
        tempo2 = tempo['description']

        humidade = dicionario['main']
        humidade2 = humidade['humidity']
        temperatura = humidade['temp_min']
        temperatura2 = f'{temperatura:.0f}'
        nivel_mar = humidade['sea_level']

        vento = dicionario['wind']
        vento2 = vento['speed']
        print('')
        linha(50)
        print('\n\t\t\t',Fore.BLUE+nome,
            '\nCéu:'+Fore.RESET,tempo2.capitalize(),
            Fore.BLUE+'\nHumidade:'+Fore.RESET,humidade2,
            Fore.BLUE+'\nNivel do mar:'+Fore.RESET,nivel_mar,
            Fore.BLUE+'\nVelocidade do vento:'+Fore.RESET,vento2,'\n')
        print(f'{int(temperatura2)/10}')
    except:
        print('\nNao encontrado!! Por favor tente novamente\n')