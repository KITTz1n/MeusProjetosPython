import json
import requests
from colorama import Fore

class Clima:

    def __init__(self):
        pass

    def printar(linha,apikey,lang):
        
        print(Fore.BLUE+linha*'-'+Fore.RESET)

        nome_cidade = input('\nInsira a cidade:\n')
        nome_estado = input('\nInsira o estado:\n')
        nome_pais = input('\nInsira o nome do pais:\n')

        req = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={nome_cidade},{nome_estado},{nome_pais}&appid={apikey}&lang={lang}')

        dicionario = json.loads(req.text)

        try:
            nome = dicionario['name']
            tempo = dicionario['weather'][0]
            tempo2 = tempo['description']

            humidade = dicionario['main']
            humidade2 = humidade['humidity']
            nivel_mar = humidade['sea_level']

            vento = dicionario['wind']
            vento2 = vento['speed']

            print('')

            print(Fore.BLUE+linha*'-'+Fore.RESET)

            print('\n\t\t\t',Fore.BLUE+nome,
                '\nCéu:'+Fore.RESET,tempo2.capitalize(),
                Fore.BLUE+'\nHumidade:'+Fore.RESET,humidade2,
                Fore.BLUE+'\nNivel do mar:'+Fore.RESET,nivel_mar,
                Fore.BLUE+'\nVelocidade do vento:'+Fore.RESET,vento2,'\n')
        except:
            print('\nNao encontrado!! Por favor tente novamente\n')