#API filmes

#Bibliotecas
import requests
import json
from PIL import Image
import pathlib
import wget
from colorama import Fore
from deep_translator import GoogleTranslator

#Variaveis
tradutor = GoogleTranslator(source="pt",target="en")
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
    try:
        img = pathlib.Path('Poster.png')
        img.unlink()
    except:
        pass

    linha(80)
    op_pt = input('\nEscreva um nome de um filme ou sair:\n')
    op_en = tradutor.translate(op_pt)
    print('')
    linha(80)
    vezes = 0
    if op_en.upper() == 'sair':
        print('Okay')
        print('Programa Finalizado')
        sair = True
        exit()
    else:
        resultados = requicicao(op_en)
        if resultados['Response'] == 'False':
            print('\nFilme Nao Encontrado\n')
        else:
            b = resultados['Search']
            titulos_achados = {}
            if len(b) > 1:
                print('\n\tEcontramos Esses Filmes')
            elif len(b) == 1:
                print('\n\tFoi Encontrado So Esse Filme')
            for i in b:
                vezes += 1
                titulo = i['Title']
                print(f'{Fore.BLUE}{vezes}-{Fore.RESET} {titulo}')
                titulos_achados[vezes] = titulo
                if vezes == len(b):
                    print('')
                    linha(80)
                    escolha = input('\nEscolha Um Deles Para Adquirir Informacoes?\n')
                    try:
                        num_esc = int(escolha)
                        escolhido = titulos_achados[num_esc]
                        titulo_escolhido = b[num_esc-1]
                        print('')
                        linha(80)
                        print('\n\t',titulo_escolhido['Title'])
                        print('\t',titulo_escolhido['Year'])
                        wget.download(titulo_escolhido['Poster'], 'Poster.png')
                        op1 = input('\n'+Fore.BLUE+'Deseja ver o poster?\n')
                        try:
                            if op1 == 'sim':
                                print('Abrindo Poster do filme\n'+Fore.RESET)
                                img = Image.open('Poster.png')
                                img.show()
                                print('Muito obrigado!\n')
                            elif op1 == 'nao':
                                print('Okay\n')
                        except:
                            pass
                    except:
                        pass