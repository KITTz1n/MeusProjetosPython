#API filmes

#Bibliotecas
import requests
import json
from PIL import Image
import pathlib
import wget
import time
from colorama import Fore
import 

#Variaveis
req = None
apikey = 'be1cb85c'
tipo = 'movie'

#Funcao Linha de decoracao
def linha(v):
    print(Fore.BLUE + v*'-' + Fore.RESET)

#Funcao requisicao do site/API
def requicicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?apikey='+apikey+'&s='+titulo+'&type='+tipo)
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('Erro Na Conexao')
        return None

sair = False

#Enquanto nao sair
while not sair:
    linha(80)
    op = input('\nEscreva um nome de um filme (obs:escreva em ingles) ou sair:\n')
    print('')
    linha(80)
    vezes = 0
    if op.upper() == 'sair':
        print('Okay')
        print('Programa Finalizado')
        sair = True
        exit()
    else:
        resultados = requicicao(op)
        if resultados['Response'] == 'False':
            print('Filme Nao Encontrado')
        else:
            b = resultados['Search']
            titulos_achados = {}
            if len(b) > 1:
                print('\tEcontramos Esses Filmes')
            elif len(b) == 1:
                print('\tFoi Encontrado So Esse Filme')
            for i in b:
                vezes += 1
                titulo = i['Title']
                print(f'{Fore.BLUE}{vezes}-{Fore.RESET} {titulo}')
                titulos_achados[vezes] = titulo
                if vezes == len(b):
                    linha(80)
                    escolha = input('Escolha Um Deles Para Adquirir Informacoes?\n')
                    try:
                        num_esc = int(escolha)
                        escolhido = titulos_achados[num_esc]
                        titulo_escolhido = b[num_esc-1]
                        print(titulo_escolhido['Title'])
                        print(titulo_escolhido['Year'])
                        wget.download(titulo_escolhido['Poster'], 'Poster.png')
                        op1 = input('\nQuer ver o poster?\n')
                        try:
                            if op1 == 'sim':
                                print('Abrindo Poster do filme')
                                time.sleep(2)
                                img = Image.open('Poster.png')
                                img.show()
                                img2 = pathlib.Path('Poster.png')
                                img2.unlink()
                                print('Muito obrigado')
                            elif op == 'nao':
                                print('Okay')
                        except:
                            pass
                    except:
                        pass