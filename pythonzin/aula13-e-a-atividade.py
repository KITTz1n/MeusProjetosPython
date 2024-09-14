#API filmes

#Bibliotecas
import requests#serve para catar API do site
import json#serve para catar a informacao em um texto json
from PIL import Image#serve para catar e abrir imagem
import pathlib#serve para catar caminho da imagem e apaga-la
import wget#serve para baixar imagem
from colorama import Fore#serve para colorir textos
from deep_translator import GoogleTranslator#serve para traduzir textos

#Variaveis
tradutor = GoogleTranslator(source="pt",target="en")#especifica o tipo de traducao: de portugues para ingles
req = None#define uma variavel onde sera armazenada futuramente o requerimento do site
apikey = 'be1cb85c'#a chave da api,para a api e o programa funcionar
tipo = 'movie'#o filtro da pesquisa, nesse caso seria movie(filme)
sair = False#definindo uma variavel onde comeca sendo falsa

#Funcao Linha de decoracao
def linha(v):#obtendo um valor
    print(Fore.BLUE + v*'-' + Fore.RESET)#mostrar(mudar cor para azul multiplicar o traco pelo valor obtido na funcao e resetando a cor)

#Funcao requisicao do site/API
def requicicao(titulo):#passando o valor do titulo que sera perguntado futuramente no script.
    try:#tentara
        req = requests.get(f'http://www.omdbapi.com/?apikey={apikey}&s={titulo}&type={tipo}')#requerimento do site da API

        dicionario = json.loads(req.text)#guardando o texto da resposta em json em uma variavel
        return dicionario#retorna o valor de dicionario
    except:#se nao conseguir
        print('Erro Na Conexao')#mostrar que houve um erro na conexao do cliente que usou o programa
        return None#retornando None(nada)

#Enquanto nao sair
while not sair:
    try:#tentar
        img = pathlib.Path('Poster.png')#armazenar a imagem em uma variavel
        img.unlink()#apagar a imagem armazenada
    except:#se nao conseguir
        pass#passar
    linha(80)#linha decoracao

    op_pt = input('\nEscreva um nome de um filme ou sair:\n')#pergunta o nome ou sair
    op_en = tradutor.translate(op_pt)#traduz para ingles a resposta

    print('')#pula linha
    vezes = 0

    if op_pt == 'sair':#se a opcao em portugues for = a sair 
        print('Okay!\nPrograma Finalizado\n')#mostrar: okay
                                             #         programa finalizado
        sair = True#define a varivel sair para verdade
        linha(80)#linha decorativa
        exit()#finaliza o programa
    else:
        linha(80)#linha decorativa
        resultados = requicicao(op_en)#armazena o resultado da funcao chamada que eu mesmo criei onde pede o valor do titulo que seria nesse caso o valor da opcao em ingles
        if resultados['Response'] == 'False':#se o resultado nao for achado
            print('\nFilme Nao Encontrado\n')#mostrar: filme nao encontrado
        else:#se nao
            b = resultados['Search']#armazena em uma variavel o valor do search encontrado na variavel resultados
            titulos_achados = {}#cria uma lista dos titulos achados
            if len(b) > 1:#se a quantidade de titulos achados for > 1
                print('\n\tEcontramos Esses Filmes')#mostrar: Encontramos esses filmes
            elif len(b) == 1:#se a quantidade de titulos for igual a 1
                print('\n\tFoi Encontrado So Esse Filme')#mostrar: Foi encontrado so esse filme
            for i in b:#cada 'i' em b(search do resultados)
                vezes += 1#somar 1 a quantidade de vezes
                titulo = i['Title']#armazenando o titulo de cada um
                print(f'{Fore.BLUE}{vezes}-{Fore.RESET} {titulo}')#mostrando a quantidade e mostrando o titulo
                titulos_achados[vezes] = titulo#armazenando na lista
                if vezes == len(b):#se a quantidade for = a quantidade de titulos achados no b(search do resultados)
                    print('')#linha vazia
                    linha(80)#linha decorativa
                    escolha = input('\nEscolha Um Deles Para Adquirir Informacoes?\n')#armazena a escolha do titulo onde dara mais informacao
                    try:#tentar
                        num_esc = int(escolha)#armazena o valor da escolha
                        escolhido = titulos_achados[num_esc]#procura esse valor da escolha na lista de titulos achados
                        titulo_escolhido = b[num_esc-1]#armazena o titulo escolhido corretamente, sendo num-1 pois a lista comeca pelo indice zero.
                        print('')#linha vazia
                        linha(80)#linha decorativa
                        print('\n\t',titulo_escolhido['Title'])#mostra o titulo escolhido pelo cliente
                        print('\t',titulo_escolhido['Year'])#mostra o ano onde o filme inserido pelo cliente foi lancado
                        wget.download(titulo_escolhido['Poster'], 'Poster.png')#baixando o poster do filme inserido pelo cliente.
                        op1 = input('\n'+Fore.BLUE+'Deseja ver o poster?\n')#pergunta se o cliente deseja ver o poster
                        try:#tentar
                            if op1 == 'sim':#se a resposta for sim
                                print('Abrindo Poster do filme\n'+Fore.RESET)#mostrar que ta abrindo o poster
                                img = Image.open('Poster.png')#procura a imagem do poster
                                img.show()#mostra a imagem do poster
                                print('Muito obrigado!\n')#agradece
                            elif op1 == 'nao':#se a resposta for nao
                                print('Okay\n')#mostrar okay e finalizar
                        except:#se nao conseguir

                            pass#passar

                    except:#se nao conseguir

                        pass#passar